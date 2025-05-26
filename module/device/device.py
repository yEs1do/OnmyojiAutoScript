from win32gui import IsWindow

import os
import psutil
import pywintypes
from collections import deque
from datetime import datetime
import time
# Patch pkg_resources before importing adbutils and uiautomator2
from module.device.pkg_resources import get_distribution
# Just avoid being removed by import optimization
_ = get_distribution

from module.device.env import IS_WINDOWS
from module.base.timer import Timer
from module.config.utils import get_server_next_update
from module.device.app_control import AppControl
from module.device.control import Control
from module.device.platform2 import Platform
from module.device.screenshot import Screenshot
from module.exception import (GameNotRunningError,
                              GameStuckError,
                              GameWaitTooLongError,
                              GameTooManyClickError,
                              RequestHumanTakeover,
                              EmulatorNotRunningError)
from module.logger import logger



class Device(Platform, Screenshot, Control, AppControl):
    _screen_size_checked = False
    detect_record = set()
    click_record = deque(maxlen=15)
    stuck_timer = Timer(60, count=60).start()
    stuck_timer_long = Timer(300, count=300).start()
    stuck_long_wait_list = ['BATTLE_STATUS_S', 'PAUSE', 'LOGIN_CHECK']

    def __init__(self, *args, **kwargs):
        max_retries = 3
        success = False
        last_exception = None  # 记录最后一次异常

        for trial in range(1, max_retries + 1):  # trial从1开始更符合语义
            try:
                super().__init__(*args, **kwargs)
                if IS_WINDOWS:
                    self._validate_window_handle()
                success = True
                break  # 成功则跳出循环

            except (EmulatorNotRunningError, pywintypes.error) as e:
                last_exception = e
                # ------------------------- 异常处理分支 -------------------------
                # (1) 窗口句柄无效错误 (Windows API error 1400)
                if isinstance(e, pywintypes.error) and e.winerror == 1400:
                    logger.warning(f"窗口句柄无效，清理残留进程 (第{trial}次重试/共{max_retries}次)")
                    self.force_cleanup()

                # (2) 模拟器未运行错误
                elif isinstance(e, EmulatorNotRunningError):
                    logger.warning(f"模拟器未运行，尝试启动 (第{trial}次重试/共{max_retries}次)")
                    self.emulator_start()

                # (3) 其他已知异常
                else:
                    self.config.notifier.push(title=self.config.task, content=f"遇到异常 [{type(e).__name__}]，准备重试 (第{trial}次/共{max_retries}次)")
                    logger.warning(f"遇到异常 [{type(e).__name__}]，准备重试 (第{trial}次/共{max_retries}次)")
                    self.force_cleanup()

        # ------------------------- 最终状态判断 -------------------------
        if not success:
            logger.critical(f"模拟器启动失败，已达最大重试次数 {max_retries} 次，最后一次错误: {last_exception}")
            self.config.notifier.push(title=self.config.task, content=f"模拟器启动失败{max_retries}次，错误类型: {type(last_exception).__name__}")
            self.force_cleanup()
            # 抛出异常时携带原始错误栈信息
            raise RequestHumanTakeover("设备初始化失败") from last_exception

        # Auto-fill emulator info
        if IS_WINDOWS and self.config.script.device.emulatorinfo_type == 'auto':
            _ = self.emulator_instance

        self.screenshot_interval_set()

        # Auto-select the fastest screenshot method
        if self.config.script.device.screenshot_method == 'auto':
            self.run_simple_screenshot_benchmark()

    def _validate_window_handle(self):
        """Windows平台专用句柄验证"""
        # 添加快速检查
        if hasattr(self, '_screenshot_handle_num') and not IsWindow(getattr(self, '_screenshot_handle_num', 0)):
            raise pywintypes.error(1400, "GetWindowRect", "无效窗口句柄")
        try:
            # 触发窗口属性检查
            _ = self.screenshot_size
        except pywintypes.error as e:
            if e.winerror == 1400:
                logger.error("窗口句柄验证失败")
                raise pywintypes.error(e.args)  # 重新抛出给上层捕获
            raise

    def force_cleanup(self):
        """精准终止当前模拟器实例关联进程"""
        logger.info('尝试清理模拟器进程')
        port = self.get_port_from_serial()
        if port is None:
            logger.error('无法获取有效端口号，跳过清理')
            return

        # 获取监听该端口的进程
        listeners = []
        for conn in psutil.net_connections(kind='tcp'):
            if conn.status == 'LISTEN' and conn.laddr.port == port:
                listeners.append(conn.pid)

        if not listeners:
            logger.info(f'端口 {port} 无监听进程')
            return

        # 终止进程树
        killed = []
        for pid in listeners:
            try:
                proc = psutil.Process(pid)
                # 终止子进程
                for child in proc.children(recursive=True):
                    child.kill()
                    killed.append(f"{child.name()}({child.pid})")
                # 终止主进程
                proc.kill()
                killed.append(f"{proc.name()}({proc.pid})")
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                logger.warning(f'进程终止失败: {e}')

        # 日志输出
        if killed:
            logger.info(f'已清理端口 {port} 进程: {", ".join(killed)}')
        else:
            logger.warning(f'端口 {port} 无权限终止进程')

        # 补充ADB清理
        os.system(f'adb -s {self.serial} kill-server')
        logger.info(f'已重置ADB连接: {self.serial}, 请稍等')
        time.sleep(3)

    def get_port_from_serial(self):
        """
        从serial中提取端口号
        Returns:
            int: 端口号，提取失败返回None
        """
        if ':' not in self.serial:
            logger.warning(f'Serial格式异常，无端口号: {self.serial}')
            return None

        try:
            _, port = self.serial.split(':', 1)
            return int(port)
        except ValueError:
            logger.error(f'端口号非数字: {port}')
            return None

    def run_simple_screenshot_benchmark(self):
        """
        Perform a screenshot method benchmark, test 3 times on each method.
        The fastest one will be set into config.
        """
        logger.info('run_simple_screenshot_benchmark')
        # Check resolution first
        # self.resolution_check_uiautomator2()
        # Perform benchmark
        from module.daemon.benchmark import Benchmark
        bench = Benchmark(config=self.config, device=self)
        method = bench.run_simple_screenshot_benchmark()
        # Set
        self.config.script.device.screenshot_method = method
        self.config.save()

    def handle_night_commission(self, daily_trigger='21:00', threshold=30):
        """
        Args:
            daily_trigger (int): Time for commission refresh.
            threshold (int): Seconds around refresh time.

        Returns:
            bool: If handled.
        """
        update = get_server_next_update(daily_trigger=daily_trigger)
        now = datetime.now()
        diff = (update.timestamp() - now.timestamp()) % 86400
        if threshold < diff < 86400 - threshold:
            return False

        # if GET_MISSION.match(self.image, offset=True):
        #     logger.info('Night commission appear.')
        #     self.click(GET_MISSION)
        #     return True

        return False

    def screenshot(self):
        """
        Returns:
            np.ndarray:
        """
        self.stuck_record_check()

        try:
            super().screenshot()
        except RequestHumanTakeover as e:
            raise RequestHumanTakeover

        if self.handle_night_commission():
            super().screenshot()

        return self.image

    def release_during_wait(self):
        # Scrcpy server is still sending video stream,
        # stop it during wait
        # self.config.script.device.screenshot_method = 'scrcpy'
        if self.config.script.device.screenshot_method == 'scrcpy':
            self._scrcpy_server_stop()
        if self.config.Emulator_ScreenshotMethod == 'nemu_ipc':
            self.nemu_ipc_release()

    def stuck_record_add(self, button):
        """
        当你要设置这个时候检测为长时间的时候，你需要在这里添加
        如果取消后，需要在`stuck_record_clear`中清除
        :param button:
        :return:
        """
        self.detect_record.add(str(button))
        logger.info(f'Add stuck record: {button}')

    def stuck_record_clear(self):
        self.detect_record = set()
        self.stuck_timer.reset()
        self.stuck_timer_long.reset()

    def stuck_record_check(self):
        """
        Raises:
            GameStuckError:
        """
        reached = self.stuck_timer.reached()
        reached_long = self.stuck_timer_long.reached()

        if not reached:
            return False
        if not reached_long:
            for button in self.stuck_long_wait_list:
                if button in self.detect_record:
                    return False

        logger.warning('Wait too long')
        logger.warning(f'Waiting for {self.detect_record}')
        self.stuck_record_clear()

        if self.app_is_running():
            raise GameWaitTooLongError(f'Wait too long')
        else:
            raise GameNotRunningError('Game died')

    def handle_control_check(self, button):
        self.stuck_record_clear()
        self.click_record_add(button)
        self.click_record_check()

    def click_record_add(self, button):
        self.click_record.append(str(button))

    def click_record_clear(self):
        self.click_record.clear()

    def click_record_remove(self, button):
        """
        Remove a button from `click_record`

        Args:
            button (Button):

        Returns:
            int: Number of button removed
        """
        removed = 0
        for _ in range(self.click_record.maxlen):
            try:
                self.click_record.remove(str(button))
                removed += 1
            except ValueError:
                # Value not in queue
                break

        return removed

    def click_record_check(self):
        """
        Raises:
            GameTooManyClickError:
        """
        count = {}
        for key in self.click_record:
            count[key] = count.get(key, 0) + 1
        count = sorted(count.items(), key=lambda item: item[1])
        if count[0][1] >= 12:
            logger.warning(f'Too many click for a button: {count[0][0]}')
            logger.warning(f'History click: {[str(prev) for prev in self.click_record]}')
            self.click_record_clear()
            raise GameTooManyClickError(f'Too many click for a button: {count[0][0]}')
        if len(count) >= 2 and count[0][1] >= 6 and count[1][1] >= 6:
            logger.warning(f'Too many click between 2 buttons: {count[0][0]}, {count[1][0]}')
            logger.warning(f'History click: {[str(prev) for prev in self.click_record]}')
            self.click_record_clear()
            raise GameTooManyClickError(f'Too many click between 2 buttons: {count[0][0]}, {count[1][0]}')

    def disable_stuck_detection(self):
        """
        Disable stuck detection and its handler. Usually uses in semi auto and debugging.
        """
        logger.info('Disable stuck detection')

        def empty_function(*arg, **kwargs):
            return False

        self.click_record_check = empty_function
        self.stuck_record_check = empty_function

    def app_start(self):
        if not self.config.script.error.handle_error:
            logger.critical('No app stop/start, because HandleError disabled')
            logger.critical('Please enable Alas.Error.HandleError or manually login to AzurLane')
            raise RequestHumanTakeover
        super().app_start()
        self.stuck_record_clear()
        self.click_record_clear()

    def app_stop(self):
        if not self.config.script.error.handle_error:
            logger.critical('No app stop/start, because HandleError disabled')
            logger.critical('Please enable Alas.Error.HandleError or manually login to AzurLane')
            raise RequestHumanTakeover
        super().app_stop()
        self.stuck_record_clear()
        self.click_record_clear()


if __name__ == "__main__":
    device = Device(config="oa")
    # cv2.imshow("imgSrceen", device.screenshot())  # 显示
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

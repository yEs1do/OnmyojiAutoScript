# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import time

import asyncio
import cv2
import inflection
import json
import os
import re
import zerorpc
import zmq
from cached_property import cached_property
from datetime import datetime, timedelta
from module.server.i18n import I18n
from multiprocessing.queues import Queue
from pathlib import Path
from pydantic import ValidationError
from threading import Thread
from typing import Callable

from module.base.decorator import del_cached_property
from module.base.utils import load_module
from module.config.config import Config
from module.config.utils import convert_to_underscore
from module.device.device import Device
from module.exception import *
from module.logger import logger, error_path, get_filename


class Script:
    def __init__(self, config_name: str = 'oas') -> None:
        self.device = None
        self.device_status = False  # 模拟器状态 True:运行中，False:已关闭
        self.server = None
        self.state_queue: Queue = None
        self.gui_update_task: Callable = None  # 回调函数, gui进程注册当每次config更新任务的时候更新gui的信息
        self.config_name = config_name
        self.failure_record = {}
        # 运行loop的线程
        self.loop_thread: Thread = None
        self.start_loop_count = 1

    @cached_property
    def config(self) -> "Config":
        try:
            from module.config.config import Config
            config = Config(config_name=self.config_name)
            return config
        except RequestHumanTakeover:
            logger.critical('Request human takeover')
            exit(1)
        except Exception as e:
            logger.exception(e)
            exit(1)

    # @cached_property
    # def device(self) -> "Device":
    #     try:
    #         from module.device.device import Device
    #         device = Device(config=self.config)
    #         return device
    #     except RequestHumanTakeover:
    #         logger.critical('Request human takeover')
    #         exit(1)
    #     except Exception as e:
    #         logger.exception(e)
    #         exit(1)

    @cached_property
    def checker(self):
        """
        占位函数，在alas中是检查服务器是否正常的
        :return:
        """
        return None

    def save_error_log(self, task='taskname', error_type='Error'):
        """
        Save last 60 screenshots in ./log/error/<timestamp>
        Save logs to ./log/error/<timestamp>/log.txt
        """
        from module.base.utils import save_image
        from module.handler.sensitive_info import (handle_sensitive_image,
                                                   handle_sensitive_logs)
        if self.config.script.error.save_error:

            folder = f'{error_path}/{task}/{error_type}'
            filename = get_filename(self.config.config_name.upper())
            error_path_base = f'{folder}/{filename}'
            error_log_path = f'{error_path_base}.log'
            error_image_path = f'{error_path_base}.png'
            Path(folder).mkdir(parents=True, exist_ok=True)
            save_image(self.device.image, error_image_path)
            with open(logger.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                start = 0
                for index, line in enumerate(lines):
                    line = line.strip(' \r\t\n')
                    if re.match('^═{15,}$', line):
                        start = index
                lines = lines[start - 2:]
                lines = handle_sensitive_logs(lines)
            with open(error_log_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            # asyncio.run(self.config.pushtg.telegram_send(title, error_path_image, error_path_log))
            self.config.notifier.send_push(task, error_type, self.device.image, error_log_path)

    def init_server(self, port: int) -> int:
        """
        初始化zerorpc服务，返回端口号
        :return:
        """
        self.server = zerorpc.Server(self)
        try:
            self.server.bind(f'tcp://127.0.0.1:{port}')
            return port
        except zmq.error.ZMQError:
            logger.error(f"Ocr server cannot bind on port {port}")
            return None

    def run_server(self) -> None:
        """
        启动zerorpc服务
        :return:
        """
        self.server.run()

    def gui_args(self, task: str) -> str:
        """
        获取给gui显示的参数
        :return:
        """
        return self.config.gui_args(task=task)

    def gui_menu(self) -> str:
        """
        获取给gui显示的菜单
        :return:
        """
        return self.config.gui_menu

    def gui_task(self, task: str) -> str:
        """
        获取给gui显示的任务 的参数的具体值
        :return:
        """
        return self.config.model.gui_task(task=task)

    def gui_set_task(self, task: str, group: str, argument: str, value) -> bool:
        """
        设置给gui显示的任务 的参数的具体值
        :return:
        """
        # 验证参数
        task = convert_to_underscore(task)
        group = convert_to_underscore(group)
        argument = convert_to_underscore(argument)
        # pandtic验证
        if isinstance(value, str):
            if len(value) == 8:
                try:
                    value = datetime.strptime(value, '%H:%M:%S').time()
                except ValueError:
                    pass

        path = f'{task}.{group}.{argument}'
        task_object = getattr(self.config.model, task, None)
        group_object = getattr(task_object, group, None)
        argument_object = getattr(group_object, argument, None)

        if argument_object is None:
            logger.error(f'Set arg {task}.{group}.{argument}.{value} failed')
            return False

        try:
            setattr(group_object, argument, value)
            argument_object = getattr(group_object, argument, None)
            logger.info(f'Set arg {task}.{group}.{argument}.{argument_object}')
            self.config.save()  # 我是没有想到什么方法可以使得属性改变自动保存的
            return True
        except ValidationError as e:
            logger.error(e)
            return False

    @zerorpc.stream
    def gui_mirror_image(self):
        """
        获取给gui显示的镜像
        :return: cv2的对象将 numpy 数组转换为字节串。接下来MsgPack 进行序列化发送方将图像数据转换为字节串
        """
        # return msgpack.packb(cv2.imencode('.jpg', self.device.screenshot())[1].tobytes())
        img = cv2.cvtColor(self.device.screenshot(), cv2.COLOR_RGB2BGR)
        self.device.stuck_record_clear()
        ret, buffer = cv2.imencode('.jpg', img)
        yield buffer.tobytes()

    def _gui_update_tasks(self) -> None:
        """
        获取更新任务后 pending waiting 的任务 和 当前的任务的数据。打包给gui显示
        :return:
        """
        data = {}
        pending = []
        waiting = []
        task = {}
        if self.config.task is not None and self.config.task.next_run < datetime.now():
            task["name"] = self.config.task.command
            task["next_run"] = str(self.config.task.next_run)
        data["task"] = task

        for p in self.config.pending_task[1:]:
            item = {"name": p.command, "next_run": str(p.next_run)}
            pending.append(item)

        for w in self.config.waiting_task:
            item = {"name": w.command, "next_run": str(w.next_run)}
            waiting.append(item)

        data["pending"] = pending
        data["waiting"] = waiting

        if self.gui_update_task is not None:
            self.gui_update_task(data)

    def _gui_set_status(self, status: str) -> None:
        """
        设置给gui显示的状态
        :param status: 可以在gui中显示的状态 有 "Init", "Empty"(不显示), "Run"(运行中), "Error", "Free"(空闲)
        :return:
        """
        data = {"status": status}
        if self.gui_update_task is not None:
            self.gui_update_task(data)

    def gui_task_list(self) -> str:
        """
        获取给gui显示的任务列表
        :return:
        """
        result = {}
        for key, value in self.config.model.dict().items():
            if isinstance(value, str):
                continue
            if key == "restart":
                continue
            if "scheduler" not in value:
                continue

            scheduler = value["scheduler"]
            item = {"enable": scheduler["enable"],
                    "next_run": str(scheduler["next_run"])}
            key = self.config.model.type(key)
            result[key] = item
        return json.dumps(result)

    def wait_until(self, future):
        """
        Wait until a specific time.

        Args:
            future (datetime):

        Returns:
            bool: True if wait finished, False if config changed.
        """
        future = future + timedelta(seconds=1)
        self.config.start_watching()
        while 1:
            if datetime.now() > future:
                return True
            # if self.stop_event is not None:
            #     if self.stop_event.is_set():
            #         logger.info("Update event detected")
            #         logger.info(f"[{self.config_name}] exited. Reason: Update")
            #         exit(0)

            time.sleep(5)

            if self.config.should_reload():
                return False

    def countdown(self, num, action):
        """
        倒计时函数，参数为倒计时的总秒数
        """
        for i in range(num, 0, -1):
            logger.warning(f"{i} seconds to {action}")  # 动态刷新当前剩余时间
            time.sleep(1)
        logger.warning("倒计时完成！")

    def get_wait_task(self, task) -> str:
        logger.hr(f"模拟器状态 {self.device_status}", level=1)
        logger.info(f'Wait `{I18n.trans_zh_cn(task.command)}` ({task.next_run})')

    def get_next_task(self) -> str:
        """
        获取下一个任务的名字, 大驼峰。
        :return:
        """
        while 1:
            task = self.config.get_next()
            self.config.task = task
            if self.state_queue:
                self.state_queue.put({"schedule": self.config.get_schedule_data()})

            if task.next_run > datetime.now():
                # logger.info(f'Wait until {task.next_run} for task `{task.command}`')

                close_game_time = self.config.script.optimization.close_game_time
                close_emulator_time = self.config.script.optimization.close_emulator_time

                close_game_time_flag = False if close_game_time.hour == 0 and close_game_time.minute == 0 and close_game_time.second == 0 else True
                close_emulator_time_flag = False if close_emulator_time.hour == 0 and close_emulator_time.minute == 0 and close_emulator_time.second == 0 else True

                close_game_time = timedelta(hours=close_game_time.hour, minutes=close_game_time.minute,
                                            seconds=close_game_time.second)
                close_emulator_time = timedelta(hours=close_emulator_time.hour, minutes=close_emulator_time.minute,
                                                seconds=close_emulator_time.second)

                if close_emulator_time_flag and task.next_run > datetime.now() + close_emulator_time:
                    # self.config.notifier.push(title='CloseMuMu',content=f'Wait `{task.command}` {str(task.next_run.time())}')
                    if self.device_status:
                        wait_time = 30
                        logger.warning(f"等待{wait_time}秒后, 关闭模拟器")
                        time.sleep(wait_time)
                        self.device.emulator_stop()
                        self.device_status = False
                        self.device.release_during_wait()
                    self.get_wait_task(task)
                    if not self.wait_until(task.next_run):
                        del_cached_property(self, 'config')
                        continue
                elif close_game_time_flag and task.next_run > datetime.now() + close_game_time:
                    try:
                        if self.device_status:
                            wait_time = 10
                            logger.warning(f"等待{wait_time}秒后, 关闭游戏")
                            time.sleep(wait_time)
                            self.device.app_stop()
                            self.device.release_during_wait()
                    except Exception as e:
                        logger.error("app stop error")
                        logger.error(e)
                    self.get_wait_task(task)
                    if not self.wait_until(task.next_run):
                        del_cached_property(self, 'config')
                        continue
                else:
                    logger.warning(f"等待中, 无需任何操作")
                    self.get_wait_task(task)
                    if self.device_status:
                        self.device.release_during_wait()
                    if not self.wait_until(task.next_run):
                        del_cached_property(self, 'config')
                        continue
            break

        return task.command

    def run(self, command: str) -> bool:
        """

        :param command:  大写驼峰命名的任务名字
        :return:
        """

        if command == 'start' or command == 'goto_main':
            logger.error(f'Invalid command `{command}`')

        try:
            self.device.screenshot()
            module_name = 'script_task'
            module_path = str(Path.cwd() / 'tasks' / command / (module_name + '.py'))
            logger.info(f'module_path: {module_path}, module_name: {module_name}')
            task_module = load_module(module_name, module_path)
            task_module.ScriptTask(config=self.config, device=self.device).run()
        except TaskEnd:
            return True
        except GameNotRunningError as e:
            logger.warning(e)
            self.config.task_call('Restart')
            return True
        except Exception as e:
            error_type = type(e).__name__  # 获取异常类型名称
            if isinstance(e, (GameWaitTooLongError, GameTooManyClickError, GamePageUnknownError, GameStuckError, GameBugError, FileNotFoundError)):
                logger.error(e)
                logger.warning(f'{error_type}, Game will be restarted in 10 seconds')
                self.device.sleep(10)
                self.config.task_call('Restart')
            elif isinstance(e, (ScriptError, RequestHumanTakeover)):
                logger.critical(e)
            else:
                logger.exception(e)
            self.save_error_log(task=command, error_type=error_type)
            return False

    def loop(self):
        """
        调度器主循环
        """
        # 初始化日志
        logger.set_file_logger(self.config_name)

        # 重置状态
        logger.info(f'[准备] 正在重置状态...')
        self.failure_record = {}
        self.device = None
        self.device_status = False
        is_first_task = True
        stop_requested = False
        self.config.model.running_task = None

        logger.info(f'[启动] 调度器循环开始 | 配置: {self.config_name}')
        try:
            while not stop_requested:
                try:
                    # ------------------------- 获取任务 -------------------------
                    task = self.get_next_task()
                    task_chinese_name = I18n.trans_zh_cn(task)
                    logger.info(f'[任务] 获取到待执行任务 | {task_chinese_name}')

                    # ------------------------- 跳过首次重启任务 -------------------------
                    if is_first_task and task == 'Restart':
                        logger.info('[任务] 跳过启动时的重启任务')
                        self.config.task_delay(task='Restart', success=True, server=True)
                        del_cached_property(self, 'config')
                        is_first_task = False
                        continue

                    # ------------------------- 设备重连逻辑 -------------------------
                    if not (self.device_status and self.device):
                        logger.warning('[设备] 检测到设备断开，尝试重新连接')
                        self.device = Device(self.config)
                        self.device_status = True
                        logger.info('[设备] 重连成功')

                    # ------------------------- 执行前清理 -------------------------
                    if self.device and self.device_status:
                        self.device.stuck_record_clear()
                        self.device.click_record_clear()
    
                    # ------------------------- 任务执行 -------------------------
                    logger.hr(f'{task_chinese_name} Start', 0)
                    self.config.model.running_task = task
                    success = self.run(inflection.camelize(task))
                    self.config.model.running_task = None
                    logger.hr(f'{task_chinese_name} End', 0)
                    is_first_task = False
                    del_cached_property(self, 'config')
    
                    # ------------------------- 失败处理 -------------------------
                    if success:
                        self.start_loop_count = 1
                        self.failure_record[task] = 0
                        continue
                    else:
                        failed = self.failure_record.get(task, 0) + 1
                        self.failure_record[task] = failed
                        MAX_FAIL_COUNT = 3

                        logger.info(f'[任务统计] 任务: {task_chinese_name} | 累计失败次数: {failed}/{MAX_FAIL_COUNT}')

                        if failed >= MAX_FAIL_COUNT:
                            logger.critical(f'[错误] 任务连续失败超过阈值 | 任务: {task_chinese_name} | 次数: {failed}/{MAX_FAIL_COUNT}')
                            stop_requested = True

                            # 失败次数超限，关闭任务
                            # task_name = convert_to_underscore(task)
                            # task_object = getattr(self.config.model, task_name, None)
                            # scheduler = getattr(task_object, 'scheduler', None)
                            # scheduler.enable = False
                            # self.config.save()

                            # 失败次数超限, 默认任务执行成功
                            self.config.task_delay(task, success=True, server=True)

                            self.config.notifier.push(title={task_chinese_name}, content=f"失败次数超限, 默认任务执行成功")

                            logger.error('[错误] 退出调度器')
                            exit(1)
    
                except Exception as e:
                    error_type = type(e).__name__  # 获取异常类型名称
                    logger.error(f'[异常] 循环运行崩溃: {error_type} | {str(e)}', exc_info=True)
                    self.config.notifier.push(title="循环崩溃", content=str(e))
                    stop_requested = True
                finally:
                    if stop_requested:
                        logger.info('[资源] 开始释放设备资源')
                        if self.device:
                            self.device.release_during_wait()
                            self.device = None
                            logger.info('[设备] 资源释放完成')
                        del_cached_property(self, 'config')
                        logger.info('[清理] 线程退出前的清理工作已完成')
        finally:
            if self.device:
                logger.warning('[安全] 最终资源清理')
                self.device.release_during_wait()
                exit(1)
    
    def start_loop(self):
        """
        循环启动控制器
        """
        # 初始化日志
        logger.set_file_logger(self.config_name)

        logger.info('[启动] 启动循环守护线程')
        max_start_loop_count = 3

        while self.start_loop_count <= max_start_loop_count:
            # 启动新线程
            self.loop_thread = Thread(target=self.loop)
            self.loop_thread.start()
            logger.info(f'[线程] 工作线程已启动 | 启动次数: {self.start_loop_count}/{max_start_loop_count}')

            # 等待线程结束（无限等待，确保线程完成）
            self.loop_thread.join()

            # 线程结束后准备启动
            self.start_loop_count += 1

            # 检查是否超过最大启动次数
            if self.start_loop_count > max_start_loop_count:
                break

        # 达到最大启动次数后的处理
        logger.error('[终止] 达到最大启动次数，系统退出')
        self.config.notifier.push(title='系统退出',content=f"[终止] 达到最大启动次数，系统退出")
        time.sleep(5)
        exit(1)


if __name__ == "__main__":
    script = Script("oa")
    script.start_loop()
    # while 1:
    # script = Script("oas3")
    # device = Device("oas3")
    # device.app_start()
    # time.sleep(10)
    # logger.info('Start app')
    # device.app_stop()
    # logger.info('Stop app')
    # time.sleep(5)
    # device.emulator_stop()
    # time.sleep(5)
    # del_cached_property(script, 'device')
    # del_cached_property(script, 'config')
    # script.start_loop()
    # script.save_error_log(title='ad')
    # locale.setlocale(locale.LC_TIME, 'chinese')
    # today = datetime.now()
    # date = today.strftime('%Y-%m-%d %A')
    # print(locale.windows_locale.values())  # Windows
    # print(date)
    # print(script.gui_task_list())
    # print(script.config.gui_menu)

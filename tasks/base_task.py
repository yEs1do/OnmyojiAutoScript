# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey

from time import sleep

import cv2
from datetime import datetime, timedelta
from numpy import uint8, fromfile
from pathlib import Path
from typing import Union

from module.atom.animate import RuleAnimate
from module.atom.click import RuleClick
from module.atom.gif import RuleGif
from module.atom.image import RuleImage
from module.atom.list import RuleList
from module.atom.long_click import RuleLongClick
from module.atom.ocr import RuleOcr
from module.atom.swipe import RuleSwipe
from module.base.timer import Timer
from module.config.config import Config
from module.config.utils import convert_to_underscore
from module.device.device import Device
from module.exception import ScriptError
from module.logger import logger, log_path, week_path, get_filename
from module.ocr.base_ocr import OcrMode
from module.server.i18n import I18n
from tasks.Component.Costume.costume_base import CostumeBase
from tasks.Component.config_base import Time
from tasks.GlobalGame.assets import GlobalGameAssets
from tasks.GlobalGame.config_emergency import FriendInvitation


class BaseTask(GlobalGameAssets, CostumeBase):
    config: Config = None
    device: Device = None

    folder: str
    name: str
    stage: str

    limit_time: timedelta = None  # 限制运行的时间，是软时间，不是硬时间
    limit_count: int = None  # 限制运行的次数
    current_count: int = None  # 当前运行的次数

    def __init__(self, config: Config, device: Device) -> None:
        """

        :rtype: object
        """
        self.config = config
        self.device = device

        self.interval_timer = {}  # 这个是用来记录每个匹配的运行间隔的，用于控制运行频率
        self.animates = {}  # 保存缓存
        self.start_time = datetime.now()  # 启动的时间
        self.check_costume(self.config.global_game.costume_config)
        # 战斗次数相关
        self.current_count = 0  # 战斗次数

    def _burst(self) -> bool:
        """
        游戏界面突发异常检测
        :return: 没有出现返回False, 其他True
        """
        appear_invitation = self.appear(self.I_G_ACCEPT)
        if not appear_invitation:
            return False
        logger.info('检测到悬赏邀请')
        invite_type = self.config.global_game.emergency.friend_invitation
        detect_record = self.device.detect_record
        match invite_type:
            case FriendInvitation.ACCEPT:
                # logger.info(f"接受全部邀请")
                click_button = self.I_G_ACCEPT
            case FriendInvitation.REJECT:
                # logger.info(f"拒绝全部邀请")
                click_button = self.I_G_REJECT
            case FriendInvitation.IGNORE:
                # logger.info(f"忽略全部邀请")
                click_button = self.I_G_IGNORE
            case FriendInvitation.ONLY_JADE:
                # logger.info(f"仅接受勾玉邀请")
                if self.appear(self.I_G_JADE):
                    click_button = self.I_G_ACCEPT
                else:
                    click_button = self.I_G_IGNORE
            case FriendInvitation.JADE_SUSHI_FOOD:
                # logger.info(f"接受勾协/体协/粮协邀请")
                if self.appear(self.I_G_JADE) or self.appear(self.I_G_CAT_FOOD) or self.appear(self.I_G_DOG_FOOD) or self.appear(self.I_G_SUSHI):
                    click_button = self.I_G_ACCEPT
                else:
                    click_button = self.I_G_IGNORE
            case _:
                raise ScriptError(f'未知的好友邀请类型: {invite_type}')
        if not click_button:
            raise ScriptError(f'未知的点击按钮类型: {invite_type}')
        while 1:
            self.device.screenshot()
            if not self.appear(target=click_button):
                # logger.info('悬赏邀请处理完成')
                break
            if self.appear_then_click(click_button, interval=0.8):
                continue
        # 长战斗场景处理（点击后可能取消战斗状态）
        self.device.detect_record = detect_record
        # 接受邀请后立即执行悬赏任务
        if click_button == self.I_G_ACCEPT:
            logger.warning('已接受悬赏邀请')
            self.set_next_run(task='WantedQuests', target=datetime.now().replace(microsecond=0))
        else:
            logger.warning(f"已忽略悬赏邀请")
        return True

    def screenshot(self):
        """
        截图 引入中间函数的目的是 为了解决如协作的这类突发的事件
        :return:
        """
        self.device.screenshot()
        # 判断勾协
        self._burst()

        return self.device.image

    def appear(self,
               target: RuleImage | RuleGif,
               interval: float = None,
               threshold: float = None):
        """

        :param target: 匹配的目标可以是RuleImage, 也可以是RuleOcr
        :param interval:
        :param threshold:
        :return:
        """
        if not isinstance(target, RuleImage) and not isinstance(target, RuleGif):
            return False

        if interval:
            if target.name in self.interval_timer:
                if self.interval_timer[target.name].limit != interval:
                    self.interval_timer[target.name] = Timer(interval)
            else:
                self.interval_timer[target.name] = Timer(interval)
            if not self.interval_timer[target.name].reached():
                return False

        appear = target.match(self.device.image, threshold=threshold)

        if appear and interval:
            self.interval_timer[target.name].reset()

        return appear

    def appear_then_click(self,
                          target: RuleImage | RuleGif,
                          action: Union[RuleClick, RuleLongClick] = None,
                          interval: float = None,
                          threshold: float = None,
                          duration: float = None):
        """
        出现了就点击，默认点击图片的位置，如果添加了click参数，就点击click的位置
        :param duration: 如果是长按，可以手动指定duration，不指定默认.单位是ms！！！！
        :param action: 可以是RuleClick, 也可以是RuleLongClick
        :param target: 可以是RuleImage后续支持RuleOcr
        :param interval:
        :param threshold:
        :return: True or False
        """
        if not isinstance(target, RuleImage) and not isinstance(target, RuleGif):
            return False

        appear = self.appear(target, interval=interval, threshold=threshold)
        if appear and not action:
            x, y = target.coord()
            self.device.click(x, y, control_name=target.name)

        elif appear and action:
            x, y = action.coord()
            if isinstance(action, RuleLongClick):
                if duration is None:
                    self.device.long_click(x, y, duration=action.duration / 1000, control_name=target.name)
                else:
                    self.device.long_click(x, y, duration=duration / 1000, control_name=target.name)
            elif isinstance(action, RuleClick):
                self.device.click(x, y, control_name=target.name)

        return appear

    def wait_until_appear(self,
                          target: RuleImage,
                          skip_first_screenshot=False,
                          wait_time: int = None) -> bool:
        """
        等待直到出现目标
        :param wait_time: 等待时间，单位秒
        :param target:
        :param skip_first_screenshot:
        :return:
        """
        wait_timer = None
        if wait_time:
            wait_timer = Timer(wait_time)
            wait_timer.start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.screenshot()
            if wait_timer and wait_timer.reached():
                logger.warning(f"Wait until appear {target.name} timeout")
                return False
            if self.appear(target):
                return True

    def wait_until_appear_then_click(self,
                                     target: RuleImage,
                                     action: Union[RuleClick, RuleLongClick] = None) -> None:
        """
        等待直到出现目标，然后点击
        :param action:
        :param target:
        :return:
        """
        self.wait_until_appear(target)
        if action is None:
            self.device.click(target.coord(), control_name=target.name)
        elif isinstance(action, RuleLongClick):
            self.device.long_click(target.coord(), duration=action.duration / 1000, control_name=target.name)
        elif isinstance(action, RuleClick):
            self.device.click(target.coord(), control_name=target.name)

    def wait_until_disappear(self, target: RuleImage) -> None:
        while 1:
            self.screenshot()
            if not self.appear(target):
                break

    def wait_until_stable(self,
                          target: RuleImage,
                          timer=Timer(0.3, count=1),
                          timeout=Timer(5, count=10),
                          skip_first_screenshot=True):
        """
        等待目标稳定，即连续多次匹配成功
        :param target:
        :param timer:
        :param timeout:
        :param skip_first_screenshot:
        :return:
        """
        target._match_init = False
        timeout.reset()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.screenshot()

            if target._match_init:
                if target.match(self.device.image):
                    if timer.reached():
                        break
                else:
                    # button.load_color(self.device.image)
                    timer.reset()
            else:
                # target.load_color(self.device.image)
                target._match_init = True

            if timeout.reached():
                logger.warning(f'Wait_until_stable({target}) timeout')
                break

    def wait_animate_stable(self, rule: RuleAnimate, interval: float = None, timeout: float = None):
        """
        不同与上面的wait_until_stable，这个将会匹配连续的两帧图片的特定区域
        @param rule:
        @param interval:
        @param timeout:
        @return:
        """
        if not isinstance(rule, RuleAnimate):
            rule = RuleAnimate(rule)
        timeout_timer = Timer(timeout).start() if timeout is not None else None
        while 1:
            self.screenshot()

            if interval:
                if rule.name in self.interval_timer:
                    if self.interval_timer[rule.name].limit != interval:
                        self.interval_timer[rule.name] = Timer(interval)
                else:
                    self.interval_timer[rule.name] = Timer(interval)
                if not self.interval_timer[rule.name].reached():
                    return False

            stable = rule.stable(self.device.image)
            if stable:
                if interval:
                    self.interval_timer[rule.name].reset()
                break

            if timeout_timer and timeout_timer.reached():
                logger.info(f'Wait_animate_stable({rule}) timeout')
                break

    def swipe(self, swipe: RuleSwipe, interval: float = None) -> None:
        """

        :param interval:
        :param swipe:
        :return:
        """
        if not isinstance(swipe, RuleSwipe):
            return

        if interval:
            if swipe.name in self.interval_timer:
                # 如果传入的限制时间不一样，则替换限制新的传入的时间
                if self.interval_timer[swipe.name].limit != interval:
                    self.interval_timer[swipe.name] = Timer(interval)
            else:
                # 如果没有限制时间，则创建限制时间
                self.interval_timer[swipe.name] = Timer(interval)
            # 如果时间还没到达，则不执行
            if not self.interval_timer[swipe.name].reached():
                return

        x1, y1, x2, y2 = swipe.coord()
        self.device.swipe(p1=(x1, y1), p2=(x2, y2), control_name=swipe.name)

        # 执行后，如果有限制时间，则重置限制时间
        if interval:
            # logger.info(f'Swipe {swipe.name}')
            self.interval_timer[swipe.name].reset()

    def click(self, click: Union[RuleClick, RuleLongClick] = None, interval: float = None) -> bool:
        """
        点击或者长按
        :param interval:
        :param click:
        :return:
        """
        if not click:
            return False

        if interval:
            if click.name in self.interval_timer:
                # 如果传入的限制时间不一样，则替换限制新的传入的时间
                if self.interval_timer[click.name].limit != interval:
                    self.interval_timer[click.name] = Timer(interval)
            else:
                # 如果没有限制时间，则创建限制时间
                self.interval_timer[click.name] = Timer(interval)
            # 如果时间还没到达，则不执行
            if not self.interval_timer[click.name].reached():
                return False

        x, y = click.coord()
        if isinstance(click, RuleLongClick):
            self.device.long_click(x=x, y=y, duration=click.duration / 1000, control_name=click.name)
        elif isinstance(click, RuleClick) or isinstance(click, RuleImage) or isinstance(click, RuleOcr):
            self.device.click(x=x, y=y, control_name=click.name)

        # 执行后，如果有限制时间，则重置限制时间
        if interval:
            self.interval_timer[click.name].reset()
            return True
        return False

    def ocr_appear(self, target: RuleOcr, interval: float = None) -> bool:
        """
        ocr识别目标
        :param interval:
        :param target:
        :return: 如果target有keyword或者是keyword存在，返回是True，否则返回False
                 但是没有指定keyword，返回的是匹配到的值，具体取决于target的mode
        """
        if not isinstance(target, RuleOcr):
            return None

        if interval:
            if target.name in self.interval_timer:
                # 如果传入的限制时间不一样，则替换限制新的传入的时间
                if self.interval_timer[target.name].limit != interval:
                    self.interval_timer[target.name] = Timer(interval)
            else:
                # 如果没有限制时间，则创建限制时间
                self.interval_timer[target.name] = Timer(interval)
            # 如果时间还没到达，则不执行
            if not self.interval_timer[target.name].reached():
                return None

        result = target.ocr(self.device.image)
        appear = False

        if not target.keyword or target.keyword == '':
            appear = False
        match target.mode:
            case OcrMode.FULL:  # 全匹配
                appear = result != (0, 0, 0, 0)
            case OcrMode.SINGLE:
                appear = result == target.keyword
            case OcrMode.DIGIT:
                appear = result == int(target.keyword)
            case OcrMode.DIGITCOUNTER:
                appear = result == target.ocr_str_digit_counter(target.keyword)
            case OcrMode.DURATION:
                appear = result == target.parse_time(target.keyword)

        if interval and appear:
            self.interval_timer[target.name].reset()

        return appear

    def ocr_appear_click(self,
                         target: RuleOcr,
                         action: Union[RuleClick, RuleLongClick] = None,
                         interval: float = None,
                         duration: float = None) -> bool:
        """
        ocr识别目标，如果目标存在，则触发动作
        :param target:
        :param action:
        :param interval:
        :param duration:
        :return:
        """
        appear = self.ocr_appear(target, interval)

        if not appear:
            return False

        if action:
            x, y = action.coord()
            self.click(action, interval)
        else:
            x, y = target.coord()
            self.device.click(x=x, y=y, control_name=target.name)
        return True

    def list_find(self, target: RuleList, name: str | list[str]) -> bool:
        """
        会一致在列表寻找目标，找到了就退出。
        如果是图片列表会一直往下找
        如果是纯文字的，会自动识别自己的位置，根据位置选择向前还是向后翻
        :param target:
        :param name:
        :return:
        """
        if target.is_image:
            while True:
                self.screenshot()
                result = target.image_appear(self.device.image, name=name)
                if result is not None:
                    return result
                x1, y1, x2, y2 = target.swipe_pos()
                self.device.swipe(p1=(x1, y1), p2=(x2, y2))

        elif target.is_ocr:
            while True:
                self.screenshot()
                result = target.ocr_appear(self.device.image, name=name)
                if isinstance(result, tuple):
                    return result

                after = True
                if isinstance(result, int) and result > 0:
                    after = True
                elif isinstance(result, int) and result < 0:
                    after = False

                x1, y1, x2, y2 = target.swipe_pos(number=1, after=after)
                self.device.swipe(p1=(x1, y1), p2=(x2, y2))
                sleep(1)  # 等待滑动完成， 还没想好如何优化

    def set_next_run(self, task: str, finish: bool = False,
                     success: bool = None, server: bool = True, target: datetime = None) -> None:
        """
        设置下次运行时间  当然这个也是可以重写的
        :param target: 可以自定义的下次运行时间
        :param server: True
        :param success: 判断是成功的还是失败的时间间隔
        :param task: 任务名称，大驼峰的
        :param finish: 是完成任务后的时间为基准还是开始任务的时间为基准
        :return:
        """
        if finish:
            start_time = datetime.now().replace(microsecond=0)
        else:
            start_time = self.start_time
        self.config.task_delay(task, start_time=start_time, success=success, server=server, target=target)

    def custom_next_run(self, task: str, custom_time: Time = None, time_delta: float = 1) -> None:
        """
        设置下次自定义运行时间
        :param task: 任务名称，大驼峰的
        :param custom_time: 可以自定义的下次运行时间
        :param time_delta: 下次运行日期为几天后，默认为第二天
        :return:
        """
        target_time = (datetime.now() + timedelta(days=time_delta)).replace(hour=custom_time.hour,
                                                                            minute=custom_time.minute,
                                                                            second=custom_time.second)
        self.set_next_run(task, target=target_time)

    def next_run_week(self, target_day: int = 1):
        """
        计算下一次运行的时间，目标是每周的特定一天。

        参数:
        target_day (int): 目标运行的日，取值1到7代表周一到周日，默认为1（周一）。
        """
        today = datetime.today()
        current_weekday = today.weekday()  # 周一为0，周日为6
        target = target_day - 1    # 将输入1-7转换为0-6
        days_diff = (target - current_weekday) % 7 or 7

        TaskName = self.config.task.command
        logger.info(f'{TaskName} done in {days_diff} days on next Week [{target_day}].')

        # 获取服务更新时间配置
        task_name = convert_to_underscore(TaskName)
        task_object = getattr(self.config.model, task_name, None)
        scheduler = getattr(task_object, 'scheduler', None)
        server_update = scheduler.server_update

        # 调用自定义函数设置下一次运行时间
        self.custom_next_run(task=TaskName,
                             custom_time=Time(hour=server_update.hour, minute=server_update.minute,
                                              second=server_update.second),
                             time_delta=days_diff)

    #  ---------------------------------------------------------------------------------------------------------------
    #
    #  ---------------------------------------------------------------------------------------------------------------
    def ui_reward_appear_click(self, screenshot=False) -> bool:
        """
        如果出现 ‘获得奖励’ 就点击
        :return:
        """
        if screenshot:
            self.screenshot()
        return self.appear_then_click(self.I_UI_REWARD, action=self.C_UI_REWARD, interval=0.4, threshold=0.6)

    def ui_get_reward(self, click_image: RuleImage or RuleOcr or RuleClick, click_interval: float = 1):
        """
        传进来一个点击图片 或是 一个ocr， 会点击这个图片，然后等待‘获得奖励’，
        最后当获得奖励消失后 退出
        :param click_interval:
        :param click_image:
        :return:
        """
        _timer = Timer(10)
        _timer.start()
        while 1:
            self.screenshot()

            if self.ui_reward_appear_click():
                sleep(0.5)
                while 1:
                    self.screenshot()
                    # 等待动画结束
                    if not self.appear(self.I_UI_REWARD, threshold=0.6):
                        logger.info('Get reward success')
                        break

                    # 一直点击
                    if self.ui_reward_appear_click():
                        continue
                break
            if _timer.reached():
                logger.warning('Get reward timeout')
                break

            if isinstance(click_image, RuleImage):
                if self.appear_then_click(click_image, interval=click_interval):
                    continue
            elif isinstance(click_image, RuleOcr):
                if self.ocr_appear_click(click_image, interval=click_interval):
                    continue
            elif isinstance(click_image, RuleClick):
                if self.click(click_image, interval=click_interval):
                    continue

        return True

    def ui_click(self, click, stop, interval=1):
        """
        循环的一个操作，直到出现stop
        :param click:
        :param stop:
        :parm interval
        :return:
        """
        while 1:
            self.screenshot()
            if self.appear(stop):
                break
            if isinstance(click, RuleImage) and self.appear_then_click(click, interval=interval):
                continue
            if isinstance(click, RuleClick) and self.click(click, interval=interval):
                continue
            elif isinstance(click, RuleOcr) and self.ocr_appear_click(click, interval=interval):
                continue

    def ui_click_until_disappear(self, click, interval: float = 1):
        """
        点击一个按钮直到消失
        :param interval:
        :param click:
        :return:
        """
        while 1:
            self.screenshot()
            if not self.appear(click):
                break
            elif self.appear_then_click(click, interval=interval):
                continue

    def load_image(file: str):
        file = Path(file)
        img = cv2.imdecode(fromfile(file, dtype=uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        height, width, channels = img.shape
        if height != 720 or width != 1280:
            logger.error(f'Image size is {height}x{width}, not 720x1280')
            return None
        return img

    def save_image(self, task_name=None, content=None, wait_time=2, image_type=False, push_flag=False):
        try:
            if task_name is None:
                task_name = "task_name"
                if self.config and self.config.task:
                    task_name = self.config.task.command

            # 设置保存图像的文件夹
            WeeklyTask = ['Duel', 'RichMan', 'ScalesSea', 'Secret', 'WeeklyTrifles', 'EternitySea', 'SixRealms', 'TrueOrochi']
            if task_name in WeeklyTask:
                folder_name = f'{week_path}/{I18n.trans_zh_cn(task_name)}'
            else:
                folder_name = f'{log_path}/{I18n.trans_zh_cn(task_name)}'
            folder_path = Path(folder_name)
            folder_path.mkdir(parents=True, exist_ok=True)

            # 截图等待时间
            if wait_time > 0:
                sleep(wait_time)
                self.screenshot()
            # 使用getattr同时检查属性和值，避免冗长的条件判断
            if getattr(self.device, 'image', None) is None:
                self.screenshot()
            image = cv2.cvtColor(self.device.image, cv2.COLOR_BGR2RGB)
            
            filename = get_filename(self.config.config_name.upper())
            image_path = folder_path / filename  # 使用pathlib路径对象

            if image_type:
                # 保存图像正常大小
                image_path = image_path.with_suffix('.png')
                params = []
            else:
                # 修改图像为.webp格式, 调整图像分辨率原来的一半
                image_path = image_path.with_suffix('.webp')
                # 调整图像分辨率
                scale_percent = 50  # 缩放到原来的一半
                width = int(image.shape[1] * scale_percent / 100)
                height = int(image.shape[0] * scale_percent / 100)
                dim = (width, height)
                image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
                # 调整图像质量并保存为WebP格式
                params = [int(cv2.IMWRITE_WEBP_QUALITY), 50]

            # 使用cv2.imencode+文件流保存（解决中文路径问题）
            ext = image_path.suffix
            ret, buf = cv2.imencode(ext, image, params)
            if ret:
                with open(image_path, 'wb') as f:
                    f.write(buf.tobytes())
                logger.info(f"截图已保存至：{image_path}")
                if push_flag:
                    self.push_notify(title=task_name, content=content if content else f"截图已保存至：{image_path}")
            else:
                self.push_notify(title=task_name, content=f"保存{image_path}, 图像编码失败")
                raise Exception("图像编码失败")
        except Exception as e:
            self.push_notify(title=task_name, content=f"保存截图异常，{e}")
            logger.error(f"保存{task_name}截图异常，{e}")

    def appear_rgb(self, target, image=None, difference: int = 10):
        """
        判断目标的平均颜色是否与图像中的颜色匹配。

        参数:
        - target: 目标对象，包含目标的文件路径和区域信息。
        - image: 输入图像，如果未提供，则使用设备捕获的图像。
        - difference: 颜色差异阈值，默认为10。

        返回:
        - 如果目标颜色与图像颜色匹配，则返回True，否则返回False。
        """
        # 如果未提供图像，则使用设备捕获的图像
        # logger.info(f"target [{target}], image [{image}]")
        if image is None:
            image = self.device.image

        # 加载图像并计算其平均颜色
        img = cv2.imread(target.file)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        average_color = cv2.mean(img_rgb)
        # logger.info(f"[{target.name}]average_color: {average_color}")

        # 提取目标区域的坐标和尺寸，并确保它们为整数
        x, y, w, h = target.roi_front
        x, y, w, h = int(x), int(y), int(w), int(h)
        # 从输入图像中提取目标区域
        img = image[y:y + h, x:x + w]
        # 计算目标区域的平均颜色
        color = cv2.mean(img)
        # logger.info(f"[{target.name}] color: {color}")

        # 比较目标图像和目标区域的颜色差异
        for i in range(3):
            if abs(average_color[i] - color[i]) > difference:
                logger.warning(f"颜色匹配失败: [{target.name}]")
                return False

        logger.info(f"颜色匹配成功: [{target.name}]")
        return True

    def push_notify(self, title=None, content=''):
        # 处理title的逻辑优化
        if title is None:
            title = 'task_name'
            if self.config and self.config.task:
                title = self.config.task.command

        # 使用getattr同时检查属性和值，避免冗长的条件判断
        if getattr(self.device, 'image', None) is None:
            self.screenshot()
        image = self.device.image

        # 发送邮件
        self.config.notifier.send_push(title=title, content=content, image=image)


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oa')
    d = Device(c)
    t = BaseTask(c, d)

    # self.config.notifier.send_mail(title=task_name, head=head, image_path=image_path)

    # t.push_notify()
    # t.save_image(content='成功找到最优挂卡', push_flag=True)
    card_type = '斗鱼'
    card_value = '118'
    t.save_image(task_name='KekkaiUtilize', push_flag=True, wait_time=0, content=f'🎉 确认蹭卡 ({card_type}: {card_value})')
    # logger.hr('INVITE FRIEND')
    # logger.hr('INVITE FRIEND', 0)
    # logger.hr('INVITE FRIEND', 1)
    # logger.hr('INVITE FRIEND', 2)
    # logger.hr('INVITE FRIEND', 3)
    # logger.hr('INVITE FRIEND')

    # datetime_now = datetime.now().strftime("%A")
    # logger.info(datetime_now)

    # # 获取当前日期
    # today = date.today()
    # # 获取星期几，返回值为 0（周一）到 6（周日）
    # weekday = today.weekday()
    # # 将数字转换为星期几的名称
    # weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    # print("今天是：", weekdays[weekday])

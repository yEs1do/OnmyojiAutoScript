# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import time
import random

from tasks.base_task import BaseTask
from tasks.Component.GeneralBattle.config_general_battle import GreenMarkType, GeneralBattleConfig
from tasks.Component.GeneralBattle.assets import GeneralBattleAssets
from module.logger import logger



class GeneralBattle(BaseTask, GeneralBattleAssets):
    """
    使用这个通用的战斗必须要求这个任务的config有config_general_battle
    """

    def run_general_battle(self, config: dict=None) -> bool:
        """
        运行脚本
        :return:
        """
        # 本人选择的策略是只要进来了就算一次，不管是不是打完了
        logger.hr("General battle start", 2)
        self.current_count += 1
        logger.info(f"Current count: {self.current_count}")
        if config is None:
            config = GeneralBattleConfig().dict()


        # 如果没有锁定队伍。那么可以根据配置设定队伍
        if not config.lock_team_enable:
            logger.info("Lock team is not enable")
            # 如果更换队伍
            if self.current_count == 1:
                self.switch_preset_team(config.preset_enable, config.preset_group, config.preset_team)

            # 点击准备按钮
            self.wait_until_appear(self.I_PREPARE_HIGHLIGHT)
            while 1:
                self.screenshot()
                if self.appear_then_click(self.I_PREPARE_HIGHLIGHT, interval=1.5):
                    continue
                if not self.appear(self.I_BUFF):
                    break
            logger.info("Click prepare ensure button")

            # 照顾一下某些模拟器慢的
            time.sleep(0.1)

        # 绿标
        self.green_mark(config.green_enable, config.green_mark)

        win = self.battle_wait(config.random_click_swipt_enable)
        if win:
            return True
        else:
            return False


    def run_general_battle_back(self, config: dict=None) -> bool:
        """
        进入挑战然后直接返回
        :param config:
        :return:
        """
        # 如果没有锁定队伍那么在点击准备后才退出的
        if not config.lock_team_enable:
            # 点击准备按钮
            self.wait_until_appear(self.I_PREPARE_HIGHLIGHT)
            while 1:
                self.screenshot()
                if self.appear_then_click(self.I_PREPARE_HIGHLIGHT, interval=1.5):
                    continue
                if not self.appear(self.I_PRESET):
                    break
            logger.info(f"Click {self.I_PREPARE_HIGHLIGHT.name}")

        # 点击返回
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_EXIT, interval=1.5):
                continue
            if self.appear(self.I_EXIT_ENSURE):
                break
        logger.info(f"Click {self.I_EXIT.name}")

        # 点击返回确认
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_EXIT_ENSURE, interval=1.5):
                continue
            if self.appear(self.I_FALSE):
                break
        logger.info(f"Click {self.I_EXIT_ENSURE.name}")

        # 点击失败确认
        self.wait_until_appear(self.I_FALSE)
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_FALSE, interval=1.5):
                continue
            if not self.appear(self.I_FALSE):
                break
        logger.info(f"Click {self.I_FALSE.name}")

        return True


    def exit_battle(self, skip_first: bool=False) -> bool:
        """
        在战斗的时候强制退出战斗
        :return:
        """
        if skip_first:
            self.screenshot()

        if not self.appear(self.I_EXIT):
            return False

        # 点击返回
        logger.info(f"Click {self.I_EXIT.name}")
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_EXIT, interval=1.5):
                continue
            if self.appear(self.I_EXIT_ENSURE):
                break

        # 点击返回确认
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_EXIT_ENSURE, interval=1.5):
                continue
            if self.appear_then_click(self.I_FALSE, interval=1.5):
                continue
            if not self.appear(self.I_EXIT):
                break

        return True


    def battle_wait(self, random_click_swipt_enable: bool) -> bool:
        """
        等待战斗结束
        :param random_click_swipt_enable:
        :return:
        """
        # 有的时候是长战斗，需要在设置stuck检测为长战斗
        # 但是无需取消设置，因为如果有点击或者滑动的话 handle_control_check会自行取消掉
        self.device.stuck_record_add('BATTLE_STATUS_S')
        # 战斗过程 随机点击和滑动 防封
        logger.info("Start battle process")
        win: bool = False
        while 1:
            self.screenshot()
            # 如果出现赢 就点击
            if self.appear(self.I_WIN, threshold=0.6):
                logger.info("Battle result is win")
                win = True
                break

            # 如果出现失败 就点击，返回False
            if self.appear(self.I_FALSE, threshold=0.6):
                logger.info("Battle result is false")
                win = False
                break

            # 如果领奖励
            if self.appear(self.I_REWARD, threshold=0.6):
                win = True
                break
            # 如果开启战斗过程随机滑动
            if random_click_swipt_enable:
                time.sleep(0.4)  # 这样的好像不对
                if 0 <= random.randint(0, 500) <= 3:  # 百分之4的概率
                    rand_type = random.randint(0, 2)
                    match rand_type:
                        case 0:
                            self.click(self.C_RANDOM_CLICK, interval=20)
                        case 1:
                            self.swipe(self.S_BATTLE_RANDOM_LEFT, interval=20)
                        case 2:
                            self.swipe(self.S_BATTLE_RANDOM_RIGHT, interval=20)
                    # 重新设置为长战斗
                    self.device.stuck_record_add('BATTLE_STATUS_S')

        # 再次确认战斗结果
        logger.info("Reconfirm the results of the battle")
        while 1:
            self.screenshot()
            if win:
                # 点击赢了
                action_click = random.choice([self.C_WIN_1, self.C_WIN_2, self.C_WIN_3])
                if self.appear_then_click(self.I_WIN, action=action_click, interval=0.5):
                    continue
                if not self.appear(self.I_WIN):
                    break
            else:
                # 如果失败且 点击失败后
                if self.appear_then_click(self.I_FALSE, threshold=0.6):
                    continue
                if not self.appear(self.I_FALSE, threshold=0.6):
                    return False
        # 最后保证能点击 获得奖励
        self.wait_until_appear(self.I_REWARD)
        logger.info("Get reward")
        while 1:
            self.screenshot()
            # 如果出现领奖励
            action_click = random.choice([self.C_REWARD_1, self.C_REWARD_2, self.C_REWARD_3])
            if self.appear_then_click(self.I_REWARD, action=action_click ,interval=1.5):
                continue
            if not self.appear(self.I_REWARD):
                break

        return win

    def green_mark(self, enable: bool=False, mark_mode: GreenMarkType=GreenMarkType.GREEN_MAIN):
        """
        绿标， 如果不使能就直接返回
        :param enable:
        :param mark_mode:
        :return:
        """
        if enable:
            logger.info("Green is enable")
            x, y = None, None
            match mark_mode:
                case GreenMarkType.GREEN_LEFT1:
                    x, y = self.C_GREEN_LEFT_1.coord()
                    logger.info("Green left 1")
                case GreenMarkType.GREEN_LEFT2:
                    x, y = self.C_GREEN_LEFT_2.coord()
                    logger.info("Green left 2")
                case GreenMarkType.GREEN_LEFT3:
                    x, y = self.C_GREEN_LEFT_3.coord()
                    logger.info("Green left 3")
                case GreenMarkType.GREEN_LEFT4:
                    x, y = self.C_GREEN_LEFT_4.coord()
                    logger.info("Green left 4")
                case GreenMarkType.GREEN_LEFT5:
                    x, y = self.C_GREEN_LEFT_5.coord()
                    logger.info("Green left 5")
                case GreenMarkType.GREEN_MAIN:
                    x, y = self.C_GREEN_MAIN.coord()
                    logger.info("Green main")

            # 等待那个准备的消失
            while 1:
                self.screenshot()
                if not self.appear(self.I_PREPARE_HIGHLIGHT):
                    break

            # 判断有无坐标的偏移
            self.appear_then_click(self.I_LOCAL)
            time.sleep(0.3)
            # 点击绿标
            self.device.click(x, y)

    def switch_preset_team(self, enable: bool=False, preset_group: int=1, preset_team: int=1):
        """
        切换预设的队伍， 要求是在不锁定队伍时的情况下
        :param enable:
        :param preset_group:
        :param preset_team:
        :return:
        """
        if not enable:
            logger.info("Preset is disable")
            return None

        logger.info("Preset is enable")
        # 点击预设按钮
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_PRESET, threshold=0.8):
                continue
            if self.appear(self.I_PRESET_ENSURE):
                break
        logger.info("Click preset button")

        # 选择预设组
        x, y = None, None
        match preset_group:
            case 1:
                x, y = self.C_PRESET_GROUP_1.coord()
            case 2:
                x, y = self.C_PRESET_GROUP_2.coord()
            case 3:
                x, y = self.C_PRESET_GROUP_3.coord()
            case 4:
                x, y = self.C_PRESET_GROUP_4.coord()
            case 5:
                x, y = self.C_PRESET_GROUP_5.coord()
            case 6:
                x, y = self.C_PRESET_GROUP_6.coord()
            case 7:
                x, y = self.C_PRESET_GROUP_7.coord()
            case _:
                x, y = self.C_PRESET_GROUP_1.coord()
        self.device.click(x, y)
        logger.info("Select preset group")

        # 选择预设的队伍
        time.sleep(0.5)
        match preset_team:
            case 1:
                x, y = self.C_PRESET_TEAM_1.coord()
            case 2:
                x, y = self.C_PRESET_TEAM_2.coord()
            case 3:
                x, y = self.C_PRESET_TEAM_3.coord()
            case 4:
                x, y = self.C_PRESET_TEAM_4.coord()
            case _:
                x, y = self.C_PRESET_TEAM_1.coord()
        self.device.click(x, y)
        logger.info("Select preset team")

        # 点击预设确认
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_PRESET_ENSURE, threshold=0.8):
                continue
            if not self.appear(self.I_PRESET_ENSURE):
                break
        logger.info("Click preset ensure")








# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from time import sleep
from datetime import datetime, time, timedelta, date
from module.config.utils import convert_to_underscore

from module.logger import logger
from module.exception import TaskEnd
from module.base.timer import Timer

from tasks.GameUi.game_ui import GameUi
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.Component.GeneralInvite.general_invite import GeneralInvite
from tasks.Component.GeneralRoom.general_room import GeneralRoom
from tasks.Orochi.script_task import ScriptTask as OrochiScriptTask
from tasks.Orochi.config import Layer
from tasks.GameUi.page import page_main, page_soul_zones, page_shikigami_records
from tasks.TrueOrochi.assets import TrueOrochiAssets
from tasks.base_task import Time

""" 真八岐大蛇 """


class ScriptTask(OrochiScriptTask, TrueOrochiAssets):

    def run(self):

        conf = self.config.true_orochi.true_orochi_config

        # 御魂切换方式一
        if self.config.true_orochi.switch_soul.enable:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul(self.config.true_orochi.switch_soul.switch_group_team)
        # 御魂切换方式二
        if self.config.true_orochi.switch_soul.enable_switch_by_name:
            self.ui_get_current_page()
            self.ui_goto(page_shikigami_records)
            self.run_switch_soul_by_name(self.config.true_orochi.switch_soul.group_name,
                                         self.config.true_orochi.switch_soul.team_name)

        self.ui_get_current_page()
        self.ui_goto(page_soul_zones)
        self.orochi_enter()
        # 检查是否出现真蛇
        battle = self.check_true_orochi(True)
        if not battle:
            # 没有发现真蛇
            logger.warning('Not find true orochi')
            logger.warning('Try to battle orochi for ten times')

            # 判断是否需要挑战十层触发真蛇
            if not conf.find_true_orochi:
                logger.info('Not find_true_orochi_help')
                self.check_times(False)
                raise TaskEnd('TrueOrochi')

            self.check_layer(Layer.TEN)
            self.check_lock(True)
            count_orochi_ten = 0
            while 1:
                self.screenshot()
                # 检查猫咪奖励
                if self.appear_then_click(self.I_PET_PRESENT, action=self.C_WIN_3, interval=1):
                    continue
                if not self.appear(self.I_OROCHI_FIRE):
                    continue
                if self.check_true_orochi(False):
                    logger.info('Find true orochi')
                    battle = True
                    break
                if count_orochi_ten >= 10:
                    logger.warning('Not find true orochi')
                    battle = False
                    break
                # 否则点击挑战
                if self.appear(self.I_OROCHI_FIRE):
                    self.ui_click_until_disappear(self.I_OROCHI_FIRE)
                    self.run_general_battle()
                    count_orochi_ten += 1
                    continue

        if not battle:
            # 如果还没有真蛇，那么就退出
            self.check_times(battle)
            raise TaskEnd('TrueOrochi')
        # 如果有真蛇，那么就开始战斗
        logger.hr('True Orochi Battle')
        while 1:
            self.screenshot()
            if self.appear(self.I_ST_CREATE_ROOM):
                break
            if self.appear_then_click(self.I_UI_CONFIRM, interval=1):
                continue
            if self.appear_then_click(self.I_ST_FIRE, interval=4):
                continue
            if self.appear_then_click(self.I_FIND_TS, interval=1):
                continue
        self.ensure_private()
        while 1:
            self.screenshot()
            if self.appear(self.I_ST_FIRE_PREPARE):
                break
            if self.appear_then_click(self.I_FIRE, interval=3, threshold=0.7):
                continue
            if self.appear_then_click(self.I_UI_CONFIRM, interval=1):
                continue
            if self.appear_then_click(self.I_ST_CREATE_ROOM, interval=1):
                continue
        # 战斗准备
        logger.info('Battle prepare')
        self.ui_click(self.I_ST_FIRE_PREPARE, self.I_BUFF)
        while 1:
            self.screenshot()
            if not self.appear(self.I_BUFF):
                break
            if self.appear_then_click(self.I_ST_AUTO_FALSE, interval=1.8):
                continue

            # 下面代码 "点击准备" 会造成，点击了准备打第一层 循环 if not self.appear(self.I_BUFF): 时候跳出while循环，导致真蛇卡在第二层
            # if self.appear_then_click(self.I_PREPARE_HIGHLIGHT, interval=1.8):
            #     continue
        self.device.stuck_record_add('BATTLE_STATUS_S')
        self.device.click_record_clear()
        logger.info("真蛇战斗开始")
        check_timer = Timer(280)
        check_timer.start()
        while 1:
            self.screenshot()
            if self.appear(self.I_GREED_GHOST):
                sleep(0.7)
                self.save_image(wait_time=5)
                self.screenshot()
                if not self.appear(self.I_GREED_GHOST):
                    continue
                # 左上角的贪吃鬼
                while 1:
                    self.screenshot()
                    if not self.appear(self.I_GREED_GHOST):
                        break
                    if self.appear_then_click(self.I_GREED_GHOST, interval=1):
                        continue
                    if self.appear_then_click(self.I_ST_FRAME, interval=1):
                        continue
                break
            if self.appear_then_click(self.I_ST_FRAME, interval=1):
                continue
            if check_timer.reached():
                logger.warning('Battle timeout')
                check_timer.reset()
                self.device.stuck_record_clear()
                self.device.stuck_record_add('BATTLE_STATUS_S')
            sleep(0.5)

        logger.info("真蛇战斗结束")
        # 真蛇战斗完成，次数加一
        conf.current_success += 1
        self.config.save()

        self.check_times(battle)

    def check_true_orochi(self, screenshot=False) -> bool:
        """
        检查是否出现真蛇（要求当前的界面必须是在御魂挑战的界面）
        :return:
        """
        if screenshot:
            self.screenshot()
        return self.appear(self.I_FIND_TS)

    def check_times(self, battle: bool):
        """
        后续的次数和时间设置
        :param battle:
        :param current_success: 这周的成功次数
        :return:
        """
        conf = self.config.true_orochi.true_orochi_config
        self.push_notify(title='真·八岐大蛇', content=f'本周已完成{conf.current_success}次，请查看截图')

        # 超过两次就说明这周打完了,设置下次运行时间为下周一，次数重置为0
        if conf.current_success >= 2:
            conf.current_success = 0
            self.config.save()
            # 设置下一次运行时间是周一
            self.next_run_week(1)
        else:
            self.set_next_run('TrueOrochi', finish=True, success=True)
        raise TaskEnd('TrueOrochi')

    def run_true_orochi(self) -> bool:
        pass


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.screenshot()

    t.run()

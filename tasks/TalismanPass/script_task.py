# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from time import sleep

from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_main, page_daily
from tasks.TalismanPass.assets import TalismanPassAssets
from tasks.TalismanPass.config import TalismanConfig, LevelReward

from module.logger import logger
from module.exception import TaskEnd
from module.base.timer import Timer
from datetime import timedelta, time, datetime


class ScriptTask(GameUi, TalismanPassAssets):

    def run(self):
        self.ui_get_current_page()
        self.ui_goto(page_main)
        self.main_goto_daily()
        con: TalismanConfig = self.config.talisman_pass.talisman

        # 收取全部奖励
        if self.in_task():
            self.get_all()
        # 收取花合战等级奖励
        self.get_flower(con.level_reward)

        now_datetime = datetime.now()
        now_time = now_datetime.time()
        if time(hour=21) > now_time > time(hour=9):
            # 如果是在9点到21点之间，那就设定下一次运行的时间为晚上21:10点
            next_run_datetime = datetime.combine(now_datetime.date(), time(hour=21, minute=10))
        else:
            next_run_datetime = datetime.combine(now_datetime.date() + timedelta(days=1), time(hour=9, minute=10))

        self.set_next_run(task='TalismanPass', target=next_run_datetime)

        raise TaskEnd('TalismanPass')

    def get_all(self):
        """
        一键收取所有的
        :return:
        """
        self.screenshot()
        if not self.appear(self.I_TP_GET_ALL):
            logger.info('No appear get all button')
        self.ui_get_reward(self.I_TP_GET_ALL)
        logger.info('Get all reward')
        sleep(0.5)

    def get_flower(self, level: LevelReward = LevelReward.TWO):
        """
        收取花合战等级奖励
        :return:
        """
        match_level = {
            LevelReward.ONE: self.I_TP_LEVEL_1,
            LevelReward.TWO: self.I_TP_LEVEL_2,
            LevelReward.THREE: self.I_TP_LEVEL_3,
        }
        self.screenshot()
        if not self.appear(self.I_RED_POINT_LEVEL):
            logger.info('No any level reward')
            return
        logger.info('Appear level reward')
        self.ui_click(self.I_RED_POINT_LEVEL, self.I_TP_GET_ALL)
        logger.info('Click level reward')
        check_timer = Timer(2)
        check_timer.start()
        while 1:
            self.screenshot()
            if self.appear_then_click(match_level[level], interval=0.8):
                logger.info(f'Select {level} reward')
                check_timer.reset()
                continue

            if self.ui_reward_appear_click(False):
                logger.info('Get reward')
                check_timer.reset()
                continue
            if check_timer.reached():
                logger.warning('No reward and break')
                break
            if self.appear_then_click(self.I_TP_GET_ALL, interval=2.1):
                logger.info('Get all reward')
                check_timer.reset()
                continue

    def in_task(self) -> bool:
        """
        判断是否在任务的界面
        :return:
        """
        self.screenshot()
        if self.appear(self.I_TP_GOTO) or self.appear(self.I_TP_EXP):
            return True
        return False


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.screenshot()

    t.run()


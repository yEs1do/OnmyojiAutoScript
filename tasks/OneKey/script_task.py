# This Python file uses the following encoding: utf-8
# @author yEs1do
# github https://github.com/yEs1do
from time import sleep
from enum import Enum
from module.logger import logger
from module.exception import TaskEnd
from module.base.timer import Timer
from datetime import timedelta, datetime

from tasks.GameUi.game_ui import GameUi
from tasks.GameUi.page import page_summon
from tasks.OneKey.assets import OneKeyAssets
from tasks.OneKey.config import ScrollNumber


class ScriptTask(GameUi, OneKeyAssets):

    def run(self): 
        # self.ui_get_current_page()
        # self.ui_goto(page_summon)
        con = self.config.one_key.one_key_config
        # 计次循环
        for i in range(con.times):
            logger.info(f'OneKey task round {i+1}/{con.times}')
            self.one_key_1(con)
        logger.info('Task over')
        self.goto_page_main(con)
        self.set_next_run(task='OneKey', success=True)
        raise TaskEnd

    def one_key_1(self, con):
        if self.wait_until_appear(self.I_OK_1, wait_time=999):
            logger.info('Appear page 1')
            self.click(self.C_OK_1, interval=1)
            sleep(con.time_1)
            if con.page_number == 1:
                logger.info('Page number is 1, return')
                return
            # 如果页面数量大于1，则继续进入下一页
            while 1:
                self.screenshot()
                if self.appear(self.I_OK_2):
                    break
                if self.appear_then_click(self.I_OVER_GHOST, interval=1):
                    continue
            logger.info('Going to page 2')
            self.one_key_2(con)
        else:
            logger.error('Failed to enter page 1')
            self.set_next_run(task='OneKey', success=False)
            raise TaskEnd
    
    def one_key_2(self, con):
        if self.wait_until_appear(self.I_OK_2, wait_time=999):
            logger.info('Appear page 2')
            self.click(self.C_OK_2, interval=1)
            sleep(con.time_2)
            if con.page_number == 2:
                logger.info('Page number is 2, return')
                return
            # 如果页面数量大于2，则继续进入下一页
            while 1:
                self.screenshot()
                if self.appear(self.I_OK_3):
                    break
                if self.appear_then_click(self.I_OVER_GHOST, interval=1):
                    continue
            logger.info('Going to page 3')
            self.one_key_3(con)
        else:
            logger.error('Failed to enter page 2')
            self.set_next_run(task='OneKey', success=False)
            raise TaskEnd
        
    def one_key_3(self, con):
        if self.wait_until_appear(self.I_OK_3, wait_time=999):
            logger.info('Appear page 3')
            self.click(self.C_OK_3, interval=1)
            sleep(con.time_3)
            if con.page_number == 3:
                logger.info('Page number is 3, return')
                return
            # 如果页面数量大于3，则继续进入下一页
            while 1:
                self.screenshot()
                if self.appear(self.I_OK_4):
                    break
                if self.appear_then_click(self.I_OVER_GHOST, interval=1):
                    continue
            logger.info('Going to page 4')
            self.one_key_4(con)
        else:
            logger.error('Failed to enter page 3')
            self.set_next_run(task='OneKey', success=False)
            raise TaskEnd
    
    def one_key_4(self, con):
        pass
    
    def goto_page_main(self, con):
        pass
    


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device
    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.screenshot()

    t.run()






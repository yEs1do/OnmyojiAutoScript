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
from tasks.OneKey.config import OneKeyConfig


class ScriptTask(GameUi, OneKeyAssets):

    def run(self):
        con = self.config.one_key.one_key_config
        # 构造资源列表（根据最大页数，动态截取）
        max_page = con.page_number
        ok_images = [self.I_OK_1, self.I_OK_2, self.I_OK_3]
        ok_clicks = [self.C_OK_1, self.C_OK_2, self.C_OK_3]
        timeouts = [con.time_1, con.time_2, con.time_3]
        # 只取前 max_page 项
        self.ok_images = ok_images[:max_page]
        self.ok_clicks = ok_clicks[:max_page]
        self.timeouts = timeouts[:max_page]

        for i in range(con.times):
            logger.info(f'OneKey task round {i+1}/{con.times}')
            self.one_key_page(con, page=0)  # 用 0-based 索引
        logger.info('Task over')
        self.goto_page_main(con)
        self.set_next_run(task='OneKey', success=True)
        raise TaskEnd

    def one_key_page(self, con, page: int):
        """
        递归处理第 page 页（0-based）。
        """
        max_page = len(self.ok_images)
        I_current = self.ok_images[page]
        C_current = self.ok_clicks[page]
        sleep_time = self.timeouts[page]

        # 等待当前页
        if not self.wait_until_appear(I_current, wait_time=999):
            logger.error(f'Failed to enter page {page+1}')
            self.set_next_run(task='OneKey', success=False)
            raise TaskEnd

        logger.info(f'Appear page {page+1}')
        self.click(C_current, interval=1)
        sleep(sleep_time)

        # 到达最后一页则返回
        if page == max_page - 1:
            logger.info(f'Page number is {page+1}, return')
            return

        # 否则等待下页出现或御魂溢出，然后递归
        next_image = self.ok_images[page+1]
        while 1:
            self.screenshot()
            if self.appear(next_image):
                break
            if self.appear_then_click(self.I_OVER_GHOST, interval=1):
                continue

        logger.info(f'Going to page {page+2}')
        self.one_key_page(con, page=page+1)
    
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






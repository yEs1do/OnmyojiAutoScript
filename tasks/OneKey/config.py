# This Python file uses the following encoding: utf-8
# @author yEs1do
# github https://github.com/yEs1do
from pydantic import BaseModel, Field
from enum import Enum
from datetime import timedelta
from pydantic import BaseModel, Field
from enum import Enum
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase, Time

# class ScrollNumber(str, Enum):
#     ONE = "卷一"
#     TWO = "卷二"
#     THREE = "卷三"
#     FOUR = "卷四"
#     FIVE = "卷五"
#     SIX = "卷六"

class OneKeyConfig(ConfigBase):
    # scroll_number: ScrollNumber = Field(default=ScrollNumber.ONE, description='scroll_number_help')
    # auto_delay_exploration: bool = Field(default=True, description='指定绘卷结束后，自动延迟探索任务，避免长时间无意义执行')
    times: int = Field(default=1, le=999, ge=1, description='循环次数')
    page_number: int = Field(default=2, ge=1, description='页面数量')
    time_1: int = Field(default=1, le=999, ge=0, description='第一间隔时间')
    time_2: int = Field(default=1, le=999, ge=0, description='第二间隔时间')
    time_3: int = Field(default=1, le=999, ge=0, description='第三间隔时间')

class OneKey(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    one_key_config: OneKeyConfig = Field(default_factory=OneKeyConfig)


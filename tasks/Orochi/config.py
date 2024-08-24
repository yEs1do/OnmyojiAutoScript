# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, time

from tasks.Component.SwitchSoul.switch_soul_config import SwitchSoulConfig as BaseSwitchSoulConfig
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase, Time
from tasks.Component.GeneralInvite.config_invite import InviteConfig
from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig


class UserStatus(str, Enum):
    LEADER = 'leader'
    MEMBER = 'member'
    ALONE = 'alone'
    WILD = 'wild'  # 还不打算实现

class Layer(str, Enum):
    ONE = '壹层'
    TWO = '贰层'
    THREE = '叁层'
    FOUR = '肆层'
    FIVE = '伍层'
    SIX = '陆层'
    SEVEN = '柒层'
    EIGHT = '捌层'
    NINE = '玖层'
    TEN = '拾层'
    ELEVEN = '悲鸣'
    TWELVE = '神罚'

class Liao30Config(BaseModel):
    # 寮30模式
    liao30_enable: bool = Field(title='寮30模式', default=True, description='只打30次结束到第二天运行')
    # 启动时间
    liao30_time: Time = Field(default=Time(hour=10), description='启动时间')

class OrochiConfig(ConfigBase):
    # 身份
    user_status: UserStatus = Field(default=UserStatus.LEADER, description='user_status_help')
    # 层数
    layer: Layer = Field(default=Layer.ELEVEN, description='layer_help')
    # 限制时间
    limit_time: Time = Field(default=Time(minute=30), description='limit_time_help')
    # 限制次数
    limit_count: int = Field(default=30, description='limit_count_help')
    # 是否开启御魂加成
    soul_buff_enable: bool = Field(default=False, description='soul_buff_enable_help')

class SwitchSoulConfig(BaseModel):
    auto_enable: bool = Field(default=False, description='auto_enable_help')
    # 十层 config
    ten_switch: str = Field(default='-1,-1', description='ten_switch_help')
    # 悲鸣 config
    eleven_switch: str = Field(default='-1,-1', description='eleven_switch_help')
    # 神罚 config
    twelve_switch: str = Field(default='-1,-1', description='twelve_switch_help')


class Orochi(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    liao30_config: Liao30Config = Field(default_factory=Liao30Config)
    orochi_config: OrochiConfig = Field(default_factory=OrochiConfig)
    invite_config: InviteConfig = Field(default_factory=InviteConfig)
    general_battle_config: GeneralBattleConfig = Field(default_factory=GeneralBattleConfig)
    switch_soul: SwitchSoulConfig = Field(default_factory=SwitchSoulConfig)


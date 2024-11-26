# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import datetime, time
from enum import Enum
from pydantic import BaseModel, ValidationError, validator, Field

class FriendInvitation(str, Enum):
    '''
    协作
    '''
    ACCEPT = 'accept'
    REJECT = 'reject'
    ONLY_JADE = 'only_jade'  # 仅接受勾玉邀请
    JADE_SUSHI_FOOD = 'jade_sushi_food'  # 勾协+粮协+体力
    IGNORE = 'ignore'

class WhenNetworkAbnormal(str, Enum):
    RESTART = 'restart'
    WAIT_10S = 'wait_10s'

class WhenNetworkError(str, Enum):
    RESTART = 'restart'

class Emergency(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    accept_now: bool = Field(default=True, description='accept_now')
=======
    # accept_now: bool = Field(default=True, description='accept_now')
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
=======
    # accept_now: bool = Field(default=True, description='accept_now')
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
    friend_invitation: FriendInvitation = Field(default=FriendInvitation.ACCEPT,description='friend_invitation_help')
    # invitation_detect_interval: int = Field(default=5, description='invitation_detect_interval_help')
    # when_network_abnormal: WhenNetworkAbnormal = Field(default=WhenNetworkAbnormal.WAIT_10S, description='when_network_abnormal_help')
    # when_network_error: WhenNetworkError = Field(default=WhenNetworkError.RESTART, description='when_network_error_help')
    # home_client_clear: bool = Field(default=True, description='home_client_clear_help')



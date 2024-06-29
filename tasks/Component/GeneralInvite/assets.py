from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralInviteAssets: 


	# Image Rule Assets
	# 中间的邀请图片 
	I_ADD_1 = RuleImage(roi_front=(592,288,114,51), roi_back=(592,288,114,51), threshold=0.9, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_1.png")
	# 最右边的邀请 
	I_ADD_2 = RuleImage(roi_front=(1039,205,100,100), roi_back=(1039,205,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_2.png")
	# description 
	I_FIRE_FAIL = RuleImage(roi_front=(1177,604,81,74), roi_back=(1177,604,81,74), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_fail.png")
	# description 
	I_FIRE = RuleImage(roi_front=(1179,602,81,87), roi_back=(1179,602,81,87), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire.png")
	# 锁定阵容的图片 
	I_LOCK = RuleImage(roi_front=(29,644,29,32), roi_back=(29,644,29,32), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_lock.png")
	# 还没有锁定阵容 
	I_UNLOCK = RuleImage(roi_front=(30,647,23,30), roi_back=(30,647,23,30), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_unlock.png")
	# 如果是到时间会退出房间，这个右边显示一个匹配的图片 
	I_MATCHING = RuleImage(roi_front=(51,574,52,114), roi_back=(51,574,52,114), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_matching.png")
	# 永生之海挑战（还未有队友的图片） 
	I_FIRE_FAIL_SEA = RuleImage(roi_front=(1160,585,100,100), roi_back=(1160,585,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_fail_sea.png")
	# description 
	I_FIRE_SEA = RuleImage(roi_front=(1160,586,100,97), roi_back=(1160,586,100,97), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_sea.png")
	# description 
	I_LOCK_SEA = RuleImage(roi_front=(781,658,27,28), roi_back=(781,658,27,28), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_lock_sea.png")
	# 永生之海 没有锁定队伍的图片 
	I_UNLOCK_SEA = RuleImage(roi_front=(781,656,27,30), roi_back=(781,656,27,30), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_unlock_sea.png")
	# 五人的队伍的第一个加号 
	I_ADD_5_1 = RuleImage(roi_front=(370,243,100,100), roi_back=(370,243,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_1.png")
	# description 
	I_ADD_5_2 = RuleImage(roi_front=(612,263,100,100), roi_back=(612,263,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_2.png")
	# description 
	I_ADD_5_3 = RuleImage(roi_front=(862,243,100,100), roi_back=(862,243,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_3.png")
	# description 
	I_ADD_5_4 = RuleImage(roi_front=(1118,228,100,100), roi_back=(1118,228,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_4.png")
	# 游戏服务器获取在线好友时等待的图片 
	I_LOAD_FRIEND = RuleImage(roi_front=(709,546,134,60), roi_back=(709,546,134,60), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_load_friend.png")
	# 左上角退出 
	I_BACK_YELLOW = RuleImage(roi_front=(19,13,58,55), roi_back=(19,13,58,55), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_back_yellow.png")
	# 点击邀请 
	I_INVITE_ENSURE = RuleImage(roi_front=(500,541,132,60), roi_back=(478,523,378,92), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_invite_ensure.png")
	# 判断是否点中好友了 
	I_SELECTED = RuleImage(roi_front=(895,373,33,32), roi_back=(380,157,568,350), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_selected.png")
	# 用来判断当前的列表是哪儿的 
	I_FLAG_1_ON = RuleImage(roi_front=(354,126,62,21), roi_back=(354,126,62,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_1_on.png")
	# description 
	I_FLAG_1_OFF = RuleImage(roi_front=(353,126,58,22), roi_back=(353,126,58,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_1_off.png")
	# description 
	I_FLAG_2_ON = RuleImage(roi_front=(465,126,61,24), roi_back=(465,126,61,24), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_2_on.png")
	# description 
	I_FLAG_2_OFF = RuleImage(roi_front=(469,127,58,21), roi_back=(469,127,58,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_2_off.png")
	# description 
	I_FLAG_3_ON = RuleImage(roi_front=(588,126,48,22), roi_back=(588,126,48,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_3_on.png")
	# description 
	I_FLAG_3_OFF = RuleImage(roi_front=(590,126,41,22), roi_back=(590,126,41,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_3_off.png")
	# description 
	I_FLAG_4_ON = RuleImage(roi_front=(713,128,34,21), roi_back=(713,128,34,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_4_on.png")
	# description 
	I_FLAG_4_OFF = RuleImage(roi_front=(703,128,53,21), roi_back=(703,128,53,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_4_off.png")
	# 永生之海添加好友 
	I_ADD_SEA = RuleImage(roi_front=(836,231,100,100), roi_back=(836,231,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_sea.png")
	# 队员不接受邀请 
	I_I_REJECT = RuleImage(roi_front=(12,226,64,61), roi_back=(12,226,64,275), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_i_reject.png")
	# 队员接受邀请 
	I_I_ACCEPT = RuleImage(roi_front=(113,225,63,72), roi_back=(113,225,63,280), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_i_accept.png")
	# 队员默认接受邀请 
	I_I_ACCEPT_DEFAULT = RuleImage(roi_front=(205,223,61,68), roi_back=(205,223,61,297), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_i_accept_default.png")
	# 不勾选 默认邀请 
	I_I_NO_DEFAULT = RuleImage(roi_front=(542,343,36,35), roi_back=(542,343,36,35), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_i_no_default.png")
	# 勾选 默认邀请 
	I_I_DEFAULT = RuleImage(roi_front=(541,342,41,39), roi_back=(541,342,41,39), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_i_default.png")
	# description 
	I_GI_CANCEL = RuleImage(roi_front=(438,407,171,55), roi_back=(438,407,171,55), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_cancel.png")
	# 队长邀请 确定 
	I_GI_SURE = RuleImage(roi_front=(670,402,175,60), roi_back=(670,402,175,60), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_sure.png")
	# 所有的组队界面都有加成 
	I_GI_BUFF = RuleImage(roi_front=(794,38,46,42), roi_back=(794,38,46,42), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_buff.png")
	# 三人御魂组队左上角的协站队伍 
	I_GI_IN_ROOM = RuleImage(roi_front=(92,17,213,64), roi_back=(92,17,213,64), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_in_room.png")


	# Image Rule Assets
	# description 
	I_GI_EMOJI_1 = RuleImage(roi_front=(27,526,55,51), roi_back=(27,526,55,51), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_emoji_1.png")
	# description 
	I_GI_EMOJI_2 = RuleImage(roi_front=(27,622,55,51), roi_back=(27,622,55,51), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_emoji_1.png")
	# 判断是不是在庭院界面 
	I_GI_HOME = RuleImage(roi_front=(361,34,34,46), roi_back=(361,34,34,46), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_home.png")
	# 判断是不是在探索界面 
	I_GI_EXPLORE = RuleImage(roi_front=(1138,119,41,48), roi_back=(1138,119,41,48), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_gi_explore.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_TIME_1 = RuleOcr(roi=(541,12,96,33), area=(541,12,96,33), mode="Single", method="Default", keyword="", name="time_1")
	# 永生之海判断时间 
	O_TIME_2 = RuleOcr(roi=(538,70,100,34), area=(538,70,100,34), mode="Single", method="Default", keyword="", name="time_2")
	# 上方好友列表的左边第一个（一般是好友） 
	O_F_LIST_1 = RuleOcr(roi=(346,94,98,41), area=(346,94,98,41), mode="Single", method="Default", keyword="", name="f_list_1")
	# Ocr-description 
	O_F_LIST_2 = RuleOcr(roi=(463,94,97,43), area=(463,94,97,43), mode="Single", method="Default", keyword="", name="f_list_2")
	# Ocr-description 
	O_F_LIST_3 = RuleOcr(roi=(580,87,91,51), area=(580,87,91,51), mode="Single", method="Default", keyword="", name="f_list_3")
	# Ocr-description 
	O_F_LIST_4 = RuleOcr(roi=(688,91,74,45), area=(688,91,74,45), mode="Single", method="Default", keyword="", name="f_list_4")
	# 寻找左侧的好友 
	O_FRIEND_NAME_1 = RuleOcr(roi=(434,185,189,345), area=(434,185,189,345), mode="Full", method="Default", keyword="", name="friend_name_1")
	# 寻找右侧的好友 
	O_FRIEND_NAME_2 = RuleOcr(roi=(729,184,196,346), area=(729,184,196,346), mode="Full", method="Default", keyword="", name="friend_name_2")
	# Ocr-description 
	O_ONLINE = RuleOcr(roi=(790,102,124,42), area=(0,0,100,100), mode="Single", method="Default", keyword="", name="online")



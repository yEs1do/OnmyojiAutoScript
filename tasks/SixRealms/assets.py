from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class SixRealmsAssets: 


	# Image Rule Assets
	# 大boss挑战 
	I_BOSS_FIRE = RuleImage(roi_front=(1128,576,100,100), roi_back=(1091,557,156,147), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_fire.png")
	# description 
	I_BOSS_TEAM_LOCK = RuleImage(roi_front=(1139,493,21,21), roi_back=(1130,487,38,43), threshold=0.95, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_team_lock.png")
	# description 
	I_BOSS_TEAM_UNLOCK = RuleImage(roi_front=(1138,497,22,21), roi_back=(1127,491,40,41), threshold=0.95, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_team_unlock.png")
	# description 
	I_BOSS_SKIP = RuleImage(roi_front=(1131,13,100,42), roi_back=(1113,5,136,62), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_skip.png")
	# description 
	I_BOSS_USE_DOUBLE = RuleImage(roi_front=(669,417,126,53), roi_back=(651,407,164,71), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_use_double.png")
	# 御神获得经验 
	I_BOSS_GET_EXP = RuleImage(roi_front=(561,109,171,45), roi_back=(492,86,281,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_get_exp.png")
	# description 
	I_BOSS_SHARE = RuleImage(roi_front=(1090,604,70,74), roi_back=(1074,587,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_share.png")
	# 结算的椒图 
	I_BOSS_SHUTU = RuleImage(roi_front=(435,46,388,46), roi_back=(338,1,573,166), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_boss_shutu.png")


	# Click Rule Assets
	# 左边的 
	C_NPC_FIRE_LEFT = RuleClick(roi_front=(423,203,153,193), roi_back=(423,203,153,193), name="npc_fire_left")
	# description 
	C_NPC_FIRE_RIGHT = RuleClick(roi_front=(740,248,181,180), roi_back=(740,248,181,180), name="npc_fire_right")
	# 中间的精英 
	C_NPC_FIRE_CENTER = RuleClick(roi_front=(620,188,174,217), roi_back=(620,188,174,217), name="npc_fire_center")
	# 默认的 
	C_ISLAND_ENTER = RuleClick(roi_front=(0,0,100,100), roi_back=(0,0,100,100), name="island_enter")
	# 右数第一个 
	C_ISLAND_ENTER_1 = RuleClick(roi_front=(1012,349,136,221), roi_back=(1012,349,136,221), name="island_enter_1")
	# description 
	C_ISLAND_ENTER_2 = RuleClick(roi_front=(825,341,143,224), roi_back=(825,341,143,224), name="island_enter_2")
	# description 
	C_ISLAND_ENTER_3 = RuleClick(roi_front=(694,338,115,222), roi_back=(694,338,115,222), name="island_enter_3")
	# description 
	C_ISLAND_ENTER_4 = RuleClick(roi_front=(501,323,141,243), roi_back=(501,323,141,243), name="island_enter_4")
	# description 
	C_ISLAND_ENTER_5 = RuleClick(roi_front=(319,332,149,237), roi_back=(319,332,149,237), name="island_enter_5")
	# description 
	C_ISLAND_ENTER_6 = RuleClick(roi_front=(162,265,136,302), roi_back=(162,265,136,302), name="island_enter_6")


	# Image Rule Assets
	# description 
	I_MENTER = RuleImage(roi_front=(346,167,30,100), roi_back=(346,167,30,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_menter.png")
	# 酒吞 
	I_MSHUTEN = RuleImage(roi_front=(46,609,70,65), roi_back=(46,609,70,65), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mshuten.png")
	# 椒图选中 
	I_MSHOUZU_SELECT = RuleImage(roi_front=(544,179,199,438), roi_back=(544,179,199,438), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mshouzu_select.png")
	# 椒图 
	I_MSHOUZU = RuleImage(roi_front=(43,608,73,67), roi_back=(43,608,73,67), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mshouzu.png")
	# 开启 
	I_MSTART = RuleImage(roi_front=(1136,575,100,100), roi_back=(1043,527,215,167), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mstart.png")
	# description 
	I_MSTART_CONFIRM = RuleImage(roi_front=(1136,575,100,100), roi_back=(1080,548,182,150), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mstart_confirm.png")
	# description 
	I_MSTART_UNCHECK = RuleImage(roi_front=(543,340,38,40), roi_back=(543,340,38,40), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mstart_uncheck.png")
	# description 
	I_MSTART_CHECK = RuleImage(roi_front=(542,340,39,41), roi_back=(542,340,39,41), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mstart_check.png")
	#  
	I_MSKIP = RuleImage(roi_front=(1117,28,58,36), roi_back=(1117,28,58,36), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mskip.png")
	# 左下角备战 
	I_PREPARE_BATTLE = RuleImage(roi_front=(33,640,48,54), roi_back=(33,640,48,54), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_prepare_battle.png")
	# 继续执行 
	I_MCONINUE = RuleImage(roi_front=(1121,578,100,100), roi_back=(1121,578,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mconinue.png")
	# 选第一个柔风 
	I_MFIRST_SKILL = RuleImage(roi_front=(255,577,141,39), roi_back=(206,550,227,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mfirst_skill.png")
	# 唤息 
	I_M_STORE = RuleImage(roi_front=(1124,594,61,57), roi_back=(1103,576,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_m_store.png")
	# 左上角退出 
	I_BACK_EXIT = RuleImage(roi_front=(11,18,51,47), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_back_exit.png")
	# 可以购买的幻息 
	I_M_STORE_ACTIVITY = RuleImage(roi_front=(1121,596,72,57), roi_back=(1107,573,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_m_store_activity.png")
	# description 
	I_MSTART_CONFIRM2 = RuleImage(roi_front=(1154,581,74,85), roi_back=(1079,535,196,177), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_mstart_confirm2.png")
	# 动画完了就有这个东西 
	I_ISLAND_TAG_FLAG = RuleImage(roi_front=(543,601,100,100), roi_back=(543,601,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_island_tag_flag.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_OCR_MAP = RuleOcr(roi=(144,227,989,376), area=(144,227,989,376), mode="Full", method="Default", keyword="", name="ocr_map")
	# Ocr-description 
	O_ISLAND_NAME = RuleOcr(roi=(88,17,148,49), area=(88,17,148,49), mode="Single", method="Default", keyword="", name="island_name")
	# 有多少钱 
	O_COIN_NUM = RuleOcr(roi=(1171,23,59,31), area=(1171,23,59,31), mode="Digit", method="Default", keyword="", name="coin_num")


	# Image Rule Assets
	# 柔风 
	I_SKILL101 = RuleImage(roi_front=(440,181,100,69), roi_back=(139,167,722,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_skill101.png")
	# description 
	I_SKILL102 = RuleImage(roi_front=(456,186,76,63), roi_back=(136,151,709,128), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_skill102.png")
	# description 
	I_SKILL103 = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_skill103.png")
	# description 
	I_SKILL104 = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_skill104.png")
	# description 
	I_SKILL_REFRESH = RuleImage(roi_front=(1196,625,44,39), roi_back=(1171,586,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_skill_refresh.png")
	# description 
	I_SELECT_0 = RuleImage(roi_front=(152,572,132,44), roi_back=(140,542,163,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_select_0.png")
	# description 
	I_SELECT_1 = RuleImage(roi_front=(424,573,137,46), roi_back=(382,544,196,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_select_1.png")
	# description 
	I_SELECT_2 = RuleImage(roi_front=(696,572,140,47), roi_back=(666,546,196,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_select_2.png")
	# 最右边的恢复生命 
	I_SELECT_3 = RuleImage(roi_front=(1016,581,145,43), roi_back=(1000,550,173,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_select_3.png")
	# 六道的金币 
	I_COIN = RuleImage(roi_front=(612,345,66,53), roi_back=(405,229,561,270), threshold=0.8, method="Template matching", file="./tasks/SixRealms/gate1/gate1_coin.png")


	# Image Rule Assets
	# 宁息刷新 
	I_STORE_REFRESH = RuleImage(roi_front=(545,596,46,47), roi_back=(519,568,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l101/l101_store_refresh.png")
	# 购买柔风 
	I_STORE_SKILL_101 = RuleImage(roi_front=(876,121,47,41), roi_back=(682,100,455,571), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l101/l101_store_skill_101.png")
	# description 
	I_STORE_EXIT = RuleImage(roi_front=(1179,586,59,56), roi_back=(1161,561,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l101/l101_store_exit.png")


	# Ocr Rule Assets
	# 刷新次数 
	O_STORE_REFRESH_TIME = RuleOcr(roi=(538,661,110,27), area=(538,661,110,27), mode="Single", method="Default", keyword="", name="store_refresh_time")


	# Image Rule Assets
	# 要花钱的界面购买 
	I_COIN_RIGHT_TOP = RuleImage(roi_front=(1065,21,40,30), roi_back=(942,10,177,112), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l102/l102_coin_right_top.png")
	# description 
	I_IMITATE = RuleImage(roi_front=(1157,598,100,100), roi_back=(1143,577,127,132), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l102/l102_imitate.png")
	# 仿造的技能 
	I_IMITATE_1 = RuleImage(roi_front=(839,194,59,44), roi_back=(794,174,358,268), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l102/l102_imitate_1.png")
	# description 
	I_IMITATE_SUCCESS = RuleImage(roi_front=(535,143,209,54), roi_back=(429,122,414,100), threshold=0.7, method="Template matching", file="./tasks/SixRealms/l102/l102_imitate_success.png")


	# Image Rule Assets
	# description 
	I_L103_EXIT = RuleImage(roi_front=(1171,587,69,70), roi_back=(1078,538,195,180), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l103/l103_exit.png")


	# Image Rule Assets
	# description 
	I_NPC_COMMON = RuleImage(roi_front=(718,232,36,40), roi_back=(684,208,100,100), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l104/l104_npc_common.png")
	# 点击挑战 
	I_NPC_FIRE = RuleImage(roi_front=(1129,585,100,100), roi_back=(1080,551,174,144), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l104/l104_npc_fire.png")
	# description 
	I_BATTLE_TEAM_UNLOCK = RuleImage(roi_front=(962,676,21,21), roi_back=(943,655,64,60), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l104/l104_battle_team_unlock.png")
	# description 
	I_BATTLE_TEAM_LOCK = RuleImage(roi_front=(961,675,21,23), roi_back=(949,662,48,50), threshold=0.8, method="Template matching", file="./tasks/SixRealms/l104/l104_battle_team_lock.png")



from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class ExplorationAssets: 


	# Click Rule Assets
	# 点击设置按钮 
	C_CLICK_SETTINGS = RuleClick(roi_front=(55,662,21,21), roi_back=(55,662,21,21), name="click_settings")
	# 选中候补出战 
	C_CLICK_STANDBY_TEAM = RuleClick(roi_front=(545,222,506,100), roi_back=(545,222,506,100), name="click_standby_team")
	# 点击全部式神按钮 
	C_CLICK_ALL_SHIKI = RuleClick(roi_front=(31,623,65,58), roi_back=(31,623,65,58), name="click_all_shiki")
	# 选中n阶式神 
	C_CLICK_N_SHIKI = RuleClick(roi_front=(146,301,45,54), roi_back=(146,301,45,54), name="click_n_shiki")
	# 位置1 
	C_CLICK_ROTATE_1 = RuleClick(roi_front=(516,582,22,21), roi_back=(516,582,22,21), name="click_rotate_1")
	# 位置2 
	C_CLICK_ROTATE_2 = RuleClick(roi_front=(650,587,21,21), roi_back=(650,587,21,21), name="click_rotate_2")
	# 位置3 
	C_CLICK_ROTATE_3 = RuleClick(roi_front=(785,587,21,21), roi_back=(785,587,21,21), name="click_rotate_3")
	# 位置4 
	C_CLICK_ROTATE_4 = RuleClick(roi_front=(921,590,21,21), roi_back=(921,590,21,21), name="click_rotate_4")


	# Image Rule Assets
	# 进入难度选择界面 
	I_E_EXPLORATION_OPEN = RuleImage(roi_front=(1077,248,37,80), roi_back=(1072,242,47,92), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_exploration_open.png")
	# 探索按钮 
	I_E_EXPLORATION_CLICK = RuleImage(roi_front=(898,518,96,42), roi_back=(898,518,96,42), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_exploration_click.png")
	# 自动轮换开着 
	I_E_AUTO_ROTATE_ON = RuleImage(roi_front=(104,649,153,44), roi_back=(104,649,153,44), threshold=0.9, method="Template matching", file="./tasks/Exploration/res/res_e_auto_rotate_on.png")
	# 自动轮换关闭 
	I_E_AUTO_ROTATE_OFF = RuleImage(roi_front=(108,650,150,46), roi_back=(108,650,150,46), threshold=0.85, method="Template matching", file="./tasks/Exploration/res/res_e_auto_rotate_off.png")
	# 成功打开设置 
	I_E_OPEN_SETTINGS = RuleImage(roi_front=(466,110,170,50), roi_back=(466,110,170,50), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_open_settings.png")
	# 选择式神稀有度 
	I_E_ENTER_CHOOSE_RARITY = RuleImage(roi_front=(34,288,62,47), roi_back=(34,288,62,47), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_enter_choose_rarity.png")
	# 候补N卡 
	I_E_N_RARITY = RuleImage(roi_front=(42,625,46,49), roi_back=(42,625,46,49), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_n_rarity.png")
	# 候补素材 
	I_E_S_RARITY = RuleImage(roi_front=(33,620,63,59), roi_back=(33,620,63,59), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_s_rarity.png")
	# 已候补出战的狗粮 
	I_E_RATATE_EXSIT = RuleImage(roi_front=(108,580,995,32), roi_back=(108,580,995,32), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_ratate_exsit.png")
	# 确定按钮 
	I_E_SURE_BUTTON = RuleImage(roi_front=(1135,426,43,37), roi_back=(1135,426,43,37), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_sure_button.png")
	# 设置按钮 
	I_E_SETTINGS_BUTTON = RuleImage(roi_front=(37,692,53,26), roi_back=(37,692,53,26), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_settings_button.png")
	# 普通怪 
	I_NORMAL_BATTLE_BUTTON = RuleImage(roi_front=(636,263,42,39), roi_back=(0,0,1279,719), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_normal_battle_button.png")
	# boss 
	I_BOSS_BATTLE_BUTTON = RuleImage(roi_front=(683,256,38,34), roi_back=(0,0,1276,719), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_boss_battle_button.png")
	# 战后奖励 
	I_BATTLE_REWARD = RuleImage(roi_front=(647,395,31,21), roi_back=(1,1,1278,718), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_battle_reward.png")
	# 妖 
	I_EXPLORATION_TITLE = RuleImage(roi_front=(1133,124,47,43), roi_back=(1133,124,47,43), threshold=0.7, method="Template matching", file="./tasks/Exploration/res/res_exploration_title.png")
	# description 
	I_BATTLE_START = RuleImage(roi_front=(555,688,39,27.5), roi_back=(221,677,561,41), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_battle_start.png")
	# description 
	I_GET_REWARD = RuleImage(roi_front=(464,231,339,44), roi_back=(464,231,339,44), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_get_reward.png")
	# description 
	I_RED_CLOSE = RuleImage(roi_front=(1027,129,41,42), roi_back=(1021,121,54,55), threshold=0.6, method="Template matching", file="./tasks/Exploration/res/res_red_close.png")
	# description 
	I_E_EXIT_CONFIRM = RuleImage(roi_front=(694,380,163,49), roi_back=(694,380,163,49), threshold=0.8, method="Template matching", file="./tasks/Exploration/res/res_e_exit_confirm.png")
	# 宝箱 
	I_TREASURE_BOX_CLICK = RuleImage(roi_front=(33,476,70,49), roi_back=(2,130,135,406), threshold=0.6, method="Template matching", file="./tasks/Exploration/res/res_treasure_box_click.png")
	# 地图宝箱
	I_MAP_BOX_CLICK = RuleImage(roi_front=(680,203,100,100), roi_back=(680,203,100,100), threshold=0.6, method="Template matching", file="./tasks/Exploration/res/res_treasure_box_click.png")


	# Ocr Rule Assets
	# 识别当前显示的章节 
	O_E_EXPLORATION_LEVEL_NUMBER = RuleOcr(roi=(1079,193,147,467), area=(1079,193,147,467), mode="Full", method="Default", keyword="", name="e_exploration_level_number")
	# 候补出战的数量 
	O_E_ALTERNATE_NUMBER = RuleOcr(roi=(1092,122,69,32), area=(1092,122,69,32), mode="DigitCounter", method="Default", keyword="", name="e_alternate_number")
	# 探索右上角 突破卷的数量 
	O_REALM_RAID_NUMBER = RuleOcr(roi=(739,11,78,37), area=(739,11,78,37), mode="DigitCounter", method="Default", keyword="", name="realm_raid_number")
	# （点出困难28时候）探索右上角 突破卷的数量 
	O_REALM_RAID_NUMBER1 = RuleOcr(roi=(936,10,82,36), area=(936,10,82,36), mode="DigitCounter", method="Default", keyword="", name="realm_raid_number1")


	# Swipe Rule Assets
	# 向上滑动章节 
	S_SWIPE_LEVEL_UP = RuleSwipe(roi_front=(1142,328,21,21), roi_back=(1143,444,21,21), mode="default", name="swipe_level_up")
	# 向下滑动章节 
	S_SWIPE_LEVEL_DOWN = RuleSwipe(roi_front=(1143,486,21,21), roi_back=(1143,367,21,23), mode="default", name="swipe_level_down")
	# 往左滑动 
	S_SWIPE_BACKGROUND_RIGHT = RuleSwipe(roi_front=(1093,148,21,21), roi_back=(397,140,21,21), mode="default", name="swipe_background_right")
	# 往右滑动 
	S_SWIPE_BACKGROUND_LEFT = RuleSwipe(roi_front=(420,142,21,21), roi_back=(1183,146,21,21), mode="default", name="swipe_background_left")
	# 滑动狗粮选择界面 
	S_SWIPE_SHIKI_TO_LEFT = RuleSwipe(roi_front=(890,587,21,21), roi_back=(351,584,21,21), mode="default", name="swipe_shiki_to_left")
	# 滑动一个式神的宽度 
	S_SWIPE_SHIKI_TO_LEFT_ONE = RuleSwipe(roi_front=(977,582,21,21), roi_back=(889,584,21,22), mode="default", name="swipe_shiki_to_left_one")



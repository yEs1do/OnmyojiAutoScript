from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DokanAssets: 


	# Click Rule Assets
	# 选择寮 
	C_DOKAN_READY_SEL = RuleClick(roi_front=(1113,179,100,100), roi_back=(1113,179,100,100), name="dokan_ready_sel")
	# 道馆随机点击安全区域 
	C_DOKAN_RANDOM_CLICK_AREA = RuleClick(roi_front=(142,294,107,555), roi_back=(142,294,107,555), name="dokan_random_click_area")
	# 道馆随机点击安全区域1：竂友突破信息 
	C_DOKAN_RANDOM_CLICK_AREA1 = RuleClick(roi_front=(42,594,10,100), roi_back=(42,594,10,100), name="dokan_random_click_area1")
	# 道馆随机点击安全区域2：切换查看队伍模式。初步测试下来这个地方最安全，除了庭院、町中、逢魔外其他各场景都可用。 
	C_DOKAN_RANDOM_CLICK_AREA2 = RuleClick(roi_front=(1122,360,10,40), roi_back=(1122,360,10,40), name="dokan_random_click_area2")
	# 道馆随机点击安全区域3 
	C_DOKAN_RANDOM_CLICK_AREA3 = RuleClick(roi_front=(333,44,107,20), roi_back=(333,44,107,20), name="dokan_random_click_area3")
	# 准备战斗 
	C_DOKAN_READY_FOR_BATTLE = RuleClick(roi_front=(42,94,1207,543), roi_back=(42,94,1207,543), name="dokan_ready_for_battle")
	# 道馆从左开始第五个绿标 
	C_DOKAN_GREEN_LEFT_5 = RuleClick(roi_front=(993,474,67,104), roi_back=(993,474,67,104), name="dokan_green_left_5")


	# Image Rule Assets
<<<<<<< HEAD
	# 道馆 
	I_DAOGUAN = RuleImage(roi_front=(462,159,100,100), roi_back=(462,159,100,100), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_daoguan.png")
	# 防守战报 
	I_FANGSHOU = RuleImage(roi_front=(35,610,75,79), roi_back=(35,610,75,79), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_fangshou.png")
	# 建立道馆  
	I_CREATE_DAOGUAN = RuleImage(roi_front=(262,630,45,62), roi_back=(262,630,45,62), threshold=0.9, method="Template matching", file="./tasks/Dokan/res/Screenshots_create_daoguan.png")
=======
	# 区域找绿标 
	I_GREEN_MARK = RuleImage(roi_front=(157,220,979,229,), roi_back=(157,220,979,229,), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/green_mark.png")
	# 道馆 
	I_DAOGUAN = RuleImage(roi_front=(462,159,100,100), roi_back=(462,159,100,100), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_daoguan.png")
	# 寮称号 
	I_GUILD_NAME_TITLE = RuleImage(roi_front=(596,191,75,43), roi_back=(596,191,75,43), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_guild_name_title.png")
	# 防守战报 
	I_FANGSHOU = RuleImage(roi_front=(35,610,75,79), roi_back=(35,610,75,79), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_fangshou.png")
	# 建立道馆  
	I_CREATE_DAOGUAN = RuleImage(roi_front=(262,630,45,62), roi_back=(262,630,45,62), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_create_daoguan.png")
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
	# 确定建立道馆 
	I_CREATE_DAOGUAN_SURE = RuleImage(roi_front=(766,409,100,55), roi_back=(766,409,100,55), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_create_daoguan_sure.png")
	# 已经建立道馆  
	I_CREATE_DAOGUAN_OK = RuleImage(roi_front=(262,630,45,62), roi_back=(262,630,45,62), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_create_daoguan_ok.png")
<<<<<<< HEAD
=======
	# 建立道馆弹出页，红色关闭 
	I_RED_CLOSE = RuleImage(roi_front=(1175,108,41,42), roi_back=(1175,108,41,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_red_close.png")
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
	# 挑战 
	I_NEWTZ = RuleImage(roi_front=(798,482,44,39), roi_back=(0,0,1047,718), threshold=0.7, method="Template matching", file="./tasks/Dokan/res/Screenshots_newtz.png")
	# 确定 
	I_OK = RuleImage(roi_front=(706,407,100,48), roi_back=(706,407,100,48), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_ok.png")
<<<<<<< HEAD
=======
	# 放弃突破 
	I_QUIT_DOKAN = RuleImage(roi_front=(60,612,53,53), roi_back=(60,612,53,53), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_quit_dokan.png")
	# 确认放弃突破 
	I_QUIT_DOKAN_SURE = RuleImage(roi_front=(669,387,144,73), roi_back=(669,387,144,73), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_quit_dokan_sure.png")
	# 管理放弃道馆over 
	I_QUIT_DOKAN_OVER = RuleImage(roi_front=(1056,211,55,35), roi_back=(1056,211,55,35), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_quit_dokan_over.png")
	# 寮友同意放弃突破 
	I_CROWD_QUIT_DOKAN = RuleImage(roi_front=(1059,244,77,71), roi_back=(1059,244,77,71), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_crowd_quit_dokan.png")
	# 再战道馆 
	I_CONTINUE_DOKAN = RuleImage(roi_front=(1177,246,71,67), roi_back=(1177,246,71,67), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/Screenshots_continue_dokan.png")
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
	# 神社->道馆 
	I_RYOU_DOKAN = RuleImage(roi_front=(476,173,62,24), roi_back=(476,173,62,24), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan.png")
	# []选择竂 
	I_RYOU_DOKAN_RYOU_SELECT = RuleImage(roi_front=(567,15,144,42), roi_back=(567,15,144,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_ryou_select.png")
	# 可选的竂列表 
	I_RYOU_DOKAN_RYOU_LIST = RuleImage(roi_front=(567,15,144,42), roi_back=(567,15,144,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_ryou_list.png")
	# 是否已经成功进入道馆，上面中间的“道馆突破”文字 
	I_RYOU_DOKAN_CHECK = RuleImage(roi_front=(567,15,144,42), roi_back=(567,15,144,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_check.png")
	# 优先攻击选项 
	I_RYOU_DOKAN_ATTACK_PRIORITY = RuleImage(roi_front=(666,672,58,25), roi_back=(666,672,58,25), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority.png")
	# 优先攻击: 见习 
	I_RYOU_DOKAN_ATTACK_PRIORITY_0 = RuleImage(roi_front=(98,170,94,43), roi_back=(98,170,94,43), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority_0.png")
	# 优先攻击: 初级 
	I_RYOU_DOKAN_ATTACK_PRIORITY_1 = RuleImage(roi_front=(342,175,96,42), roi_back=(342,175,96,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority_1.png")
	# 优先攻击: 中级 
	I_RYOU_DOKAN_ATTACK_PRIORITY_2 = RuleImage(roi_front=(585,175,89,35), roi_back=(585,175,89,35), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority_2.png")
	# 优先攻击: 高级 
	I_RYOU_DOKAN_ATTACK_PRIORITY_3 = RuleImage(roi_front=(830,175,88,41), roi_back=(830,175,88,41), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority_3.png")
	# 优先攻击: 黑脸 
	I_RYOU_DOKAN_ATTACK_PRIORITY_4 = RuleImage(roi_front=(1072,178,94,39), roi_back=(1072,178,94,39), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_priority_4.png")
	# 状态：集结等待中。检查右下角的挑战是不是灰色的。FIXME 黄色和灰色的挑战截图总是傻傻分不清，先改用OCR 
	I_RYOU_DOKAN_GATHERING = RuleImage(roi_front=(653,76,46,26), roi_back=(653,76,46,26), threshold=0.85, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_gathering.png")
	# 状态：检查右下角有没有挑战？通常是失败了，并退出来到集结界面，可重新开始点击右下角挑战进入战斗 
	I_RYOU_DOKAN_START_CHALLENGE = RuleImage(roi_front=(1132,572,89,43), roi_back=(1132,572,89,43), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_start_challenge.png")
	# 状态：达到失败次数，CD中。挑战次数恢复倒数 
	I_RYOU_DOKAN_CD1 = RuleImage(roi_front=(1068,500,146,27), roi_back=(1068,500,146,27), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_cd1.png")
	# 状态：达到失败次数，CD中。观战按钮 
	I_RYOU_DOKAN_CD = RuleImage(roi_front=(1122,566,117,74), roi_back=(1122,566,117,74), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_cd.png")
	# 状态：进入战斗，待开始，右下角图标。TODO 欠截图。 
	I_RYOU_DOKAN_IN_FIELD = RuleImage(roi_front=(1128,536,100,100), roi_back=(1128,536,100,100), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_in_field.png")
	# 馆主战等待中 
	I_DOKAN_BOSS_WAITING = RuleImage(roi_front=(603,148,130,32), roi_back=(603,148,130,32), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_dokan_boss_waiting.png")
	# 打馆主胜利 
	I_RYOU_DOKAN_WIN = RuleImage(roi_front=(628,60,45,33), roi_back=(628,60,45,33), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_win.png")
	# 打馆主失败 
	I_RYOU_DOKAN_FAIL = RuleImage(roi_front=(454,44,56,46), roi_back=(454,44,56,46), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_fail.png")
	# 状态：进入战斗，待开始，右下角图标。 
	I_RYOU_DOKAN_IN_FIELD2 = RuleImage(roi_front=(1131,562,88,48), roi_back=(1131,562,88,48), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_in_field2.png")
	# 状态：战斗结算，可能是打完小朋友了，也可能是失败了。 
	I_RYOU_DOKAN_BATTLE_OVER = RuleImage(roi_front=(571,503,106,49), roi_back=(571,503,106,49), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_battle_over.png")
	# 状态：战斗中，左上角的加油图标 
	I_RYOU_DOKAN_FIGHTING = RuleImage(roi_front=(232,36,42,19), roi_back=(232,36,42,19), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_fighting.png")
	# 状态：道馆已经结束 
	I_RYOU_DOKAN_FINISHED = RuleImage(roi_front=(658,649,91,27), roi_back=(658,649,91,27), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_finished.png")
	# 状态：道馆挑战失败，投票NO 
	I_RYOU_DOKAN_FAILED_VOTE_NO = RuleImage(roi_front=(567,15,144,42), roi_back=(567,15,144,42), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_failed_vote_no.png")
	# 道馆退出确认 
	I_RYOU_DOKAN_EXIT_ENSURE = RuleImage(roi_front=(678,395,125,56), roi_back=(678,395,125,56), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_exit_ensure.png")
	# 进入加油相关：道馆战报按钮 
	I_RYOU_DOKAN_CHEERING_SCORES = RuleImage(roi_front=(157,100,35,39), roi_back=(157,100,35,39), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_cheering_scores.png")
	# 进入加油相关：前往战斗中的竂友 
	I_RYOU_DOKAN_CHEERING_ATTACKING_SAMA = RuleImage(roi_front=(948,182,56,295), roi_back=(948,182,56,295), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/res_ryou_dokan_cheering_attacking_sama.png")
	# 场景检测：阴阳竂 
	I_SCENE_RYOU = RuleImage(roi_front=(1161,674,75,31), roi_back=(1161,674,75,31), threshold=0.8, method="Template matching", file="./tasks/Dokan/res/scene_ryou.png")


	# List Rule Assets
	# 这个是当前活跃的竂活动列表界面 
	L_RYOU_ACTIVITY_LIST = RuleList(folder="./tasks/Dokan/res", direction="vertical", mode="ocr", roi_back=(35,157,37,250), size=(42, 27), 
					 array=["道馆", "首领", "狭间"])


	# Ocr Rule Assets
<<<<<<< HEAD
=======
	# 道馆开启状态 
	O_DOKAN_STATUS = RuleOcr(roi=(492,628,222,44), area=(492,628,222,44), mode="Full", method="Default", keyword="", name="dokan_status")
>>>>>>> 2f966614481189a9805470d0d1fd6c4bcdc004d6
	# 选择寮1 
	O_DOKAN_READY_SEL1 = RuleOcr(roi=(1156,105,80,28), area=(1156,105,80,28), mode="Digit", method="Default", keyword="", name="dokan_ready_sel1")
	# 选择寮2 
	O_DOKAN_READY_SEL2 = RuleOcr(roi=(1156,255,80,28), area=(1156,255,80,28), mode="Digit", method="Default", keyword="", name="dokan_ready_sel2")
	# 选择寮3 
	O_DOKAN_READY_SEL3 = RuleOcr(roi=(1156,400,80,28), area=(1156,400,80,28), mode="Digit", method="Default", keyword="", name="dokan_ready_sel3")
	# 选择寮4 
	O_DOKAN_READY_SEL4 = RuleOcr(roi=(1156,545,80,28), area=(1156,545,80,28), mode="Digit", method="Default", keyword="", name="dokan_ready_sel4")
	# 道馆地图里找文字：万 
	O_DOKAN_MAP = RuleOcr(roi=(270,130,740,460), area=(270,130,740,460), mode="Full", method="Default", keyword="万", name="dokan_map")
	# 道馆里找文字：后开战 
	O_DOKAN_GATHERING = RuleOcr(roi=(535,75,211,29), area=(535,75,211,29), mode="Single", method="Default", keyword="开战", name="dokan_gathering")
	# 道馆里找文字：剩余突破时间 
	O_DOKAN_ATTACKING = RuleOcr(roi=(1122,546,92,51), area=(1122,546,92,51), mode="Single", method="Default", keyword="剩余", name="dokan_attacking")
	# 道馆里找文字：后挑战馆主 
	O_DOKAN_BOSS_WAITING = RuleOcr(roi=(603,148,130,32), area=(603,148,130,32), mode="Single", method="Default", keyword="馆主", name="dokan_boss_waiting")
	# 道馆里找文字：后关闭 
	O_DOKAN_SUCCEEDED = RuleOcr(roi=(655,76,49,28), area=(655,76,49,28), mode="Full", method="Default", keyword="关闭", name="dokan_succeeded")



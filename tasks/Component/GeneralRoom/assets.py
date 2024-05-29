from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralRoomAssets: 


	# List Rule Assets
	# description 
	L_TEAM_LIST = RuleList(folder="./tasks/Component/GeneralRoom", direction="vertical", mode="ocr", roi_back=(26,106,360,549), size=(216, 61), 
					 array=["全部", "探索（困难）", "觉醒业火轮", "觉醒风转符", "觉醒火灵鲤", "觉醒天雷鼓", "御魂", "日轮之陨", "永生之海", "妖气封印", "经验妖怪", "金币妖怪", "年兽", "石距", "愤怒的石距", "喷怒的石距", "结界突破", "真·八岐大蛇", "对弈社", "斗町", "连携召唤", "契灵之境"])


	# Ocr Rule Assets
	# 副本名字 
	O_GR_ZONES_NAME = RuleOcr(roi=(415,127,160,53), area=(415,127,160,53), mode="Single", method="Default", keyword="", name="gr_zones_name")


	# Image Rule Assets
	# description 
	I_CREATE_ROOM = RuleImage(roi_front=(985,600,177,58), roi_back=(396,569,813,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_room.png")
	# description 
	I_CREATE_ENSURE = RuleImage(roi_front=(813,560,129,63), roi_back=(813,560,129,63), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_ensure.png")
	# 勾选不公开的图 
	I_ENSURE_PRIVATE = RuleImage(roi_front=(748,489,36,40), roi_back=(748,489,36,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private.png")
	# 这个是还没勾选的图 
	I_ENSURE_PRIVATE_FALSE = RuleImage(roi_front=(747,489,37,40), roi_back=(747,489,37,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_false.png")
	# description 
	I_ENSURE_PRIVATE_2 = RuleImage(roi_front=(401,409,34,40), roi_back=(401,409,34,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_2.png")
	# description 
	I_ENSURE_PRIVATE_FALSE_2 = RuleImage(roi_front=(400,408,36,38), roi_back=(400,408,36,38), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_false_2.png")
	# description 
	I_CREATE_ENSURE_2 = RuleImage(roi_front=(552,489,42,55), roi_back=(552,489,42,55), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_ensure_2.png")
	# description 
	I_GR_BACK_YELLOW = RuleImage(roi_front=(19,13,53,53), roi_back=(19,13,53,53), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_gr_back_yellow.png")
	# 自动匹配 
	I_GR_AUTO_MATCH = RuleImage(roi_front=(697,598,181,63), roi_back=(697,598,181,63), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_gr_auto_match.png")
	# 刷新 
	I_GR_REFRESH = RuleImage(roi_front=(417,595,176,65), roi_back=(417,595,176,65), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_gr_refresh.png")
	# description 
	I_ENSURE_PUBLIC = RuleImage(roi_front=(400,282,35,37), roi_back=(400,282,35,37), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_public.png")
	# description 
	I_ENSURE_PUBLIC_FALSE = RuleImage(roi_front=(399,285,37,35), roi_back=(399,285,37,35), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_public_false.png")
	# description 
	I_ENSURE_PUBLIC_2 = RuleImage(roi_front=(307,490,37,40), roi_back=(307,490,37,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_public_2.png")
	# description 
	I_ENSURE_PUBLIC_FALSE_2 = RuleImage(roi_front=(307,491,38,37), roi_back=(307,491,38,37), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_public_false_2.png")



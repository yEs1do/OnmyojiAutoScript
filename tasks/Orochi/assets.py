from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class OrochiAssets: 


	# Image Rule Assets
	# 八级大蛇进入 
	I_OROCHI = RuleImage(roi_front=(55,104,295,406), roi_back=(55,104,295,406), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_orochi.png")
	# 组队 
	I_FORM_TEAM = RuleImage(roi_front=(937,591,100,100), roi_back=(937,591,100,100), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_form_team.png")
	# description 
	I_OROCHI_LOCK = RuleImage(roi_front=(575,561,22,26), roi_back=(548,546,109,62), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_orochi_lock.png")
	# description 
	I_OROCHI_UNLOCK = RuleImage(roi_front=(575,561,21,21), roi_back=(550,544,121,60), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_orochi_unlock.png")
	# 点击挑战 
	I_OROCHI_FIRE = RuleImage(roi_front=(1095,577,131,124), roi_back=(1095,577,131,124), threshold=0.6, method="Template matching", file="./tasks/Orochi/o/o_orochi_fire.png")
	# 式神录 
	I_SHI_RECORDS = RuleImage(roi_front=(821,638,48,45), roi_back=(821,638,48,45), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_shi_records.png")
	# description 
	I_OROCHI_MATCHING = RuleImage(roi_front=(62,568,44,114), roi_back=(62,568,44,114), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_orochi_matching.png")
	# 小小宠物，发现宝藏 
	I_PET_PRESENT = RuleImage(roi_front=(873,184,62,147), roi_back=(873,184,62,147), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_pet_present.png")
	# 御魂溢出 
	I_OVER_GHOST = RuleImage(roi_front=(609,410,65,28), roi_back=(609,410,65,28), threshold=0.8, method="Template matching", file="./tasks/Orochi/o/o_over_ghost.png")


	# List Rule Assets
	# 这个是御魂界面选择不同层数的 
	L_LAYER_LIST = RuleList(folder="./tasks/Orochi/res", direction="vertical", mode="ocr", roi_back=(138,130,359,500), size=(45, 88), 
					 array=["壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾", "悲", "神"])


	# Ocr Rule Assets
	# Ocr-description 
	O_O_TEST_OCR = RuleOcr(roi=(126,136,360,491), area=(126,136,360,491), mode="Full", method="Default", keyword="", name="o_test_ocr")



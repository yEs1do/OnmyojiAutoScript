from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RichManAssets: 


	# Image Rule Assets
	# 神社 
	I_GUILD_SHRINE = RuleImage(roi_front=(869,623,64,62), roi_back=(869,623,64,62), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_shrine.png")
	# 功勋商店 
	I_GUILD_STORE = RuleImage(roi_front=(651,420,212,161), roi_back=(651,420,212,161), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_store.png")
	# description 
	I_GUILD_CLOSE_RED = RuleImage(roi_front=(1029,120,53,57), roi_back=(1029,120,53,57), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_close_red.png")
	# 蓝票 
	I_GUILD_BLUE = RuleImage(roi_front=(793,179,74,80), roi_back=(793,179,74,80), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_blue.png")
	# 黑蛋碎片 
	I_GUILD_SCRAP = RuleImage(roi_front=(570,442,71,68), roi_back=(570,442,71,68), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_scrap.png")
	# 皮肤券 
	I_GUILD_SKIN = RuleImage(roi_front=(795,436,71,74), roi_back=(795,436,71,74), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_skin.png")
	# 购买检查 
	I_GUILD_CHECK_SCRAP = RuleImage(roi_front=(454,240,90,88), roi_back=(454,240,90,88), threshold=0.8, method="Template matching", file="./tasks/RichMan/guild/guild_guild_check_scrap.png")


	# Ocr Rule Assets
	# 总的功勋 
	O_GUILD_TOTAL = RuleOcr(roi=(1151,6,100,42), area=(1151,6,100,42), mode="Digit", method="Default", keyword="", name="guild_total")
	# Ocr-description 
	O_GUILD_NUMBER_BLUE = RuleOcr(roi=(888,269,25,33), area=(888,269,25,33), mode="Digit", method="Default", keyword="", name="guild_number_blue")
	# Ocr-description 
	O_GUILD_NUMBER_BLACK = RuleOcr(roi=(663,520,22,31), area=(663,520,22,31), mode="Digit", method="Default", keyword="", name="guild_number_black")
	# Ocr-description 
	O_GUILD_NUMBER_SKIN = RuleOcr(roi=(889,519,21,35), area=(889,519,21,35), mode="Digit", method="Default", keyword="", name="guild_number_skin")


	# Swipe Rule Assets
	# description 
	S_GUILD_STORE = RuleSwipe(roi_front=(807,460,46,35), roi_back=(720,214,90,34), mode="default", name="guild_store")


	# Click Rule Assets
	# description 
	C_C_SHRINE = RuleClick(roi_front=(1098,261,56,100), roi_back=(1098,261,56,100), name="c_shrine")


	# Image Rule Assets
	# 下期预览 
	I_S_NEXT_PERIOD = RuleImage(roi_front=(1083,574,90,86), roi_back=(1083,574,90,86), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_next_period.png")
	# description 
	I_S_WHITE_FIVE = RuleImage(roi_front=(769,143,77,85), roi_back=(769,143,77,85), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_white_five.png")
	# description 
	I_S_WHITE_FOUR = RuleImage(roi_front=(951,144,73,82), roi_back=(951,144,73,82), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_white_four.png")
	# 黑蛋 
	I_S_BLACK = RuleImage(roi_front=(588,143,78,83), roi_back=(588,143,78,83), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_black.png")
	# description 
	I_S_BUY_BLACK = RuleImage(roi_front=(777,508,173,60), roi_back=(777,508,173,60), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_buy_black.png")
	# description 
	I_S_BUY_WHITE_FIVE = RuleImage(roi_front=(778,512,177,56), roi_back=(778,512,177,56), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_buy_white_five.png")
	# description 
	I_S_BUY_WHITE_FOUR = RuleImage(roi_front=(779,507,173,64), roi_back=(779,507,173,64), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_buy_white_four.png")
	# description 
	I_S_CONFIRM_WHITE_FIVE = RuleImage(roi_front=(554,438,174,61), roi_back=(554,438,174,61), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_confirm_white_five.png")
	# description 
	I_S_CONFIRM_WHITE_FOUR = RuleImage(roi_front=(552,509,176,62), roi_back=(552,509,176,62), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_confirm_white_four.png")
	# description 
	I_S_CONFIRM_BLACK = RuleImage(roi_front=(552,439,180,62), roi_back=(552,439,180,62), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_confirm_black.png")
	# description 
	I_S_BUY_UP = RuleImage(roi_front=(762,412,56,54), roi_back=(762,412,56,54), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_buy_up.png")
	# description 
	I_S_CHECK_BLACK = RuleImage(roi_front=(811,225,108,178), roi_back=(811,225,108,178), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_check_black.png")
	# description 
	I_S_CHECK_WHITE_FIVE = RuleImage(roi_front=(810,222,109,182), roi_back=(810,222,109,182), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_check_white_five.png")
	# description 
	I_S_CHECK_WHITE_FOUR = RuleImage(roi_front=(808,222,113,181), roi_back=(808,222,113,181), threshold=0.8, method="Template matching", file="./tasks/RichMan/shrine/shrine_s_check_white_four.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_S_TOTAL = RuleOcr(roi=(1134,11,112,36), area=(1134,11,112,36), mode="Digit", method="Default", keyword="", name="s_total")
	# 已兑换 
	O_S_BLACK = RuleOcr(roi=(582,179,84,48), area=(582,179,84,48), mode="Single", method="Default", keyword="", name="s_black")
	# Ocr-description 
	O_S_WHITE_FIVE = RuleOcr(roi=(774,174,69,44), area=(774,174,69,44), mode="Single", method="Default", keyword="", name="s_white_five")
	# Ocr-description 
	O_S_WHITE_FOUR = RuleOcr(roi=(952,168,74,60), area=(952,168,74,60), mode="Single", method="Default", keyword="", name="s_white_four")
	# 买两个四星蛋 
	O_S_FOUR_NUMBER = RuleOcr(roi=(581,414,46,45), area=(581,414,46,45), mode="Digit", method="Default", keyword="2", name="s_four_number")


	# Image Rule Assets
	# 千物宝库 
	I_TT_ENTER = RuleImage(roi_front=(1140,585,73,76), roi_back=(1140,585,73,76), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_enter.png")
	# 确认进入 
	I_TT_CHECK = RuleImage(roi_front=(141,61,228,67), roi_back=(141,61,228,67), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_check.png")
	# description 
	I_TT_BLACK = RuleImage(roi_front=(710,176,91,90), roi_back=(453,171,589,109), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_black.png")
	# description 
	I_TT_TICKET_BULE = RuleImage(roi_front=(484,176,85,91), roi_back=(475,170,562,110), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_ticket_bule.png")
	# description 
	I_TT_AP = RuleImage(roi_front=(938,177,88,87), roi_back=(467,167,581,123), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_ap.png")
	# 提高 
	I_TT_BUY_UP = RuleImage(roi_front=(761,411,59,57), roi_back=(761,411,59,57), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_buy_up.png")
	# description 
	I_TT_BUY_CONFIRM = RuleImage(roi_front=(584,512,53,53), roi_back=(553,508,169,60), threshold=0.8, method="Template matching", file="./tasks/RichMan/tt/tt_tt_buy_confirm.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_TT_TOTOL = RuleOcr(roi=(1121,10,116,35), area=(1121,10,116,35), mode="Digit", method="Default", keyword="", name="tt_totol")
	# Ocr-description 
	O_TT_BLUE_TICKET = RuleOcr(roi=(509,307,531,92), area=(509,307,531,92), mode="Full", method="Default", keyword="2000", name="tt_blue_ticket")
	# Ocr-description 
	O_TT_BLACK = RuleOcr(roi=(498,313,528,89), area=(498,313,528,89), mode="Full", method="Default", keyword="350", name="tt_black")
	# Ocr-description 
	O_TT_AP = RuleOcr(roi=(502,311,535,91), area=(502,311,535,91), mode="Full", method="Default", keyword="300", name="tt_ap")
	# Ocr-description 
	O_TT_BUY = RuleOcr(roi=(602,509,104,61), area=(602,509,104,61), mode="Full", method="Default", keyword="", name="tt_buy")
	# Ocr-description 
	O_TT_NUMBER = RuleOcr(roi=(576,415,58,49), area=(576,415,58,49), mode="Digit", method="Default", keyword="", name="tt_number")


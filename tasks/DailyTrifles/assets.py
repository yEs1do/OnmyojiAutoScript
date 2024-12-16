from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DailyTriflesAssets: 


	# Image Rule Assets
	# description 
	I_L_FRIENDS = RuleImage(roi_front=(67,625,70,72), roi_back=(67,625,70,72), threshold=0.9, method="Template matching", file="./tasks/DailyTrifles/love/love_l_friends.png")
	# description 
	I_L_LOVE = RuleImage(roi_front=(123,625,67,72), roi_back=(123,625,67,72), threshold=0.9, method="Template matching", file="./tasks/DailyTrifles/love/love_l_love.png")
	# 一键收取 
	I_L_COLLECT = RuleImage(roi_front=(47,537,129,56), roi_back=(47,537,129,56), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/love_l_collect.png")
	# 吉闻 
	I_LUCK_MSG = RuleImage(roi_front=(22,47,46,27), roi_back=(22,47,46,27), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_luck_msg.png")
	# 一键祝福 
	I_ONE_CLICK_BLESS = RuleImage(roi_front=(1115,500,93,33), roi_back=(1115,500,93,33), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_one_click_bless.png")
	# 点击祝福 
	I_CLICK_BLESS = RuleImage(roi_front=(617,442,92,39), roi_back=(617,442,92,39), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_click_bless.png")
	# 吉闻页 
	I_LUCK_TITLE = RuleImage(roi_front=(600,52,131,67), roi_back=(600,52,131,67), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_luck_title.png")
	# 好友羁绊提升弹窗 
	I_FRIENDSHIP_UP = RuleImage(roi_front=(1147,80,27,28), roi_back=(1147,80,27,28), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/friendship_up.png")


	# Image Rule Assets
	# 礼包屋 
	I_ROOM_GIFT = RuleImage(roi_front=(1152,644,52,53), roi_back=(1127,611,103,94), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_room_gift.png")
	# description 
	I_GIFT_RECOMMEND = RuleImage(roi_front=(1186,98,53,64), roi_back=(1172,83,83,306), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_gift_recommend.png")
	# 免费一抽 
	I_GIFT_SIGN = RuleImage(roi_front=(236,129,306,218), roi_back=(236,129,306,218), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_gift_sign.png")
	# 下载拓展包弹窗 
	I_DLC_CLOSE = RuleImage(roi_front=(916,147,24,25), roi_back=(916,147,24,25), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_dlc_close.png")



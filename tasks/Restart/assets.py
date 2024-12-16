from module.atom.click import RuleClick
from module.atom.image import RuleImage
from module.atom.ocr import RuleOcr


# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RestartAssets: 


	# Image Rule Assets
	# 点击勾玉 
	I_HARVEST_JADE = RuleImage(roi_front=(732,489,34,33), roi_back=(177,451,973,141), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_jade.png")
	# 签到小图标 
	I_HARVEST_SIGN = RuleImage(roi_front=(397,500,24,34), roi_back=(70,471,889,89), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign.png")
	# description 
	I_HARVEST_SIGN_2 = RuleImage(roi_front=(592,135,100,252), roi_back=(592,135,100,252), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_2.png")
	# 999签到福袋 
	I_HARVEST_SIGN_999 = RuleImage(roi_front=(345,494,23,29), roi_back=(51,459,888,103), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_999.png")
	# 邮件小图标 
	I_HARVEST_MAIL = RuleImage(roi_front=(337,505,37,25), roi_back=(38,465,880,89), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail.png")
	# 全部收取 
	I_HARVEST_MAIL_ALL = RuleImage(roi_front=(80,622,75,64), roi_back=(80,622,75,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_all.png")
	# 有些邮件需要点击一次 
	I_HARVEST_MAIL_OPEN = RuleImage(roi_front=(163,367,45,48), roi_back=(139,86,100,487), threshold=0.9, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_open.png")
	# 确认收取邮件 
	I_HARVEST_MAIL_CONFIRM = RuleImage(roi_front=(687,543,168,64), roi_back=(687,543,168,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_confirm.png")
	# description 
	I_HARVEST_SOUL = RuleImage(roi_front=(241,497,38,36), roi_back=(68,480,930,72), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul.png")
	# description 
	I_HARVEST_MAIL_TITLE = RuleImage(roi_front=(520,48,245,41), roi_back=(520,48,245,41), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_title.png")
	# description 
	I_HARVEST_AP = RuleImage(roi_front=(721,486,31,38), roi_back=(206,462,970,134), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_ap.png")
	# 打开聊天频道会自动关闭 
	I_HARVEST_CHAT_CLOSE = RuleImage(roi_front=(639,309,35,100), roi_back=(639,309,35,100), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_chat_close.png")
	# 签到 
	I_HARVEST_SIGN_3 = RuleImage(roi_front=(291,495,33,36), roi_back=(100,473,1014,91), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_3.png")
	# description 
	I_HARVEST_SIGN_4 = RuleImage(roi_front=(587,151,100,228), roi_back=(547,123,185,281), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_4.png")
	# 点击随机御魂 
	I_HARVEST_SOUL_1 = RuleImage(roi_front=(248,501,34,37), roi_back=(165,389,929,168), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_1.png")
	# 选择第一个御魂 
	I_HARVEST_SOUL_2 = RuleImage(roi_front=(586,561,112,47), roi_back=(570,547,139,71), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_2.png")
	# description 
	I_HARVEST_SOUL_3 = RuleImage(roi_front=(313,489,188,33), roi_back=(302,472,216,60), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_3.png")
	# 寮包 
	I_HARVEST_GUILD_REWARD = RuleImage(roi_front=(244,498,41,42), roi_back=(200,403,817,157), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_guild_reward.png")
	# 宠物小屋关闭按钮 
	I_HARVEST_BACK_PET_HOUSE = RuleImage(roi_front=(20,15,70,70), roi_back=(20,15,70,70), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_back_pet_house.png")
	# 点击庭院阴阳师出现的姿度按钮 
	I_HARVEST_ZIDU = RuleImage(roi_front=(785,475,135,135), roi_back=(785,475,135,135), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_zidu.png")
	# description 
	I_HARVEST_MAIL_COPY = RuleImage(roi_front=(257,509,29,21), roi_back=(192,472,790,100), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_copy.png")


	# Click Rule Assets
	# 相同服务器多个角色选择界面,点击空白区域 确认登录 
	C_LOGIN_ENSURE_LOGIN_CHARACTER_IN_SAME_SVR = RuleClick(roi_front=(600,240,500,400), roi_back=(600,240,500,400), name="login_ensure_login_character_in_same_svr")


	# Image Rule Assets
	# 庭院卷轴打开 
	I_LOGIN_SCROOLL_OPEN = RuleImage(roi_front=(1208,609,33,83), roi_back=(1208,609,33,83), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_open.png")
	# 庭院卷轴关闭 
	I_LOGIN_SCROOLL_CLOSE = RuleImage(roi_front=(1181,634,28,39), roi_back=(1162,595,77,112), threshold=0.7, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_close.png")
	# description 
	I_LOGIN_RED_CLOSE = RuleImage(roi_front=(912,0,360,290), roi_back=(912,0,360,290), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_red_close.png")
	# description 
	I_LOGIN_YELLOW_CLOSE = RuleImage(roi_front=(29,17,46,44), roi_back=(0,0,94,86), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_yellow_close.png")
	# 用于判断是否出现登录选区的 
	I_LOGIN_8 = RuleImage(roi_front=(178,572,53,60), roi_back=(1,547,241,105), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_8.png")
	# 登录时候不观看CG视频 
	I_WATCH_VIDEO_CANCEL = RuleImage(roi_front=(466,396,130,61), roi_back=(466,396,130,61), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_watch_video_cancel.png")
	# 指定角色进入游戏,默认第一个 
	I_LOGIN_SPECIFIC_SERVE = RuleImage(roi_front=(0,0,120,120), roi_back=(0,0,120,120), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_specific_serve.png")
	# 下载插画 
	I_LOGIN_LOAD_DOWN = RuleImage(roi_front=(711,450,153,58), roi_back=(711,450,153,58), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_load_down.png")
	# 登录界面 弹出框 前往绑定 手机 
	I_LOGIN_LOGIN_GOTO_BIND_PHONE = RuleImage(roi_front=(940,430,170,150), roi_back=(940,430,170,150), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_goto_bind_phone.png")
	# 登录界面 弹出框 确定绑定手机 
	I_LOGIN_LOGIN_ENSURE_BIND_PHONE = RuleImage(roi_front=(670,460,160,100), roi_back=(670,460,160,100), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_ensure_bind_phone.png")
	# 登录界面 弹出框 取消绑定手机 
	I_LOGIN_LOGIN_CANCEL_BIND_PHONE = RuleImage(roi_front=(450,460,160,100), roi_back=(450,460,160,100), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_cancel_bind_phone.png")
	# 登录界面 弹出框 阴阳师精灵 
	I_LOGIN_LOGIN_ONMYOJI_GENIE = RuleImage(roi_front=(80,110,280,120), roi_back=(80,110,280,120), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_onmyoji_genie.png")


	# Ocr Rule Assets
	# 正在连接服务器 
	O_LOGIN_NETWORK = RuleOcr(roi=(534,649,189,39), area=(210,492,100,100), mode="Single", method="Default", keyword="正在连接服务器", name="login_network")
	# Ocr-description 
	O_LOGIN_ENTER_GAME = RuleOcr(roi=(550,567,176,56), area=(558,574,154,49), mode="Single", method="Default", keyword="进入游戏", name="login_enter_game")
	# 点击屏幕跳过 
	O_LOGIN_SKIP_1 = RuleOcr(roi=(1046,35,130,37), area=(1046,35,130,37), mode="Single", method="Default", keyword="点击屏幕跳过", name="login_skip_1")
	# 登录指定角色，默认第一个 
	O_LOGIN_SPECIFIC_SERVE = RuleOcr(roi=(110,120,350,600), area=(110,120,350,600), mode="Full", method="Default", keyword="", name="login_specific_serve")



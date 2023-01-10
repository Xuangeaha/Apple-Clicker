import sys  # 导入模块
import time
import random
import pygame
import threading
import cryptocode
import tkinter as tk
import ttkbootstrap as ttk
from win10toast import ToastNotifier

ver: str = 'beta0.8.0'  # 版本号

########## 初始化定义 ##########

apple_amount: int = 0  # 苹果数量
apple_amount_total: int = 0

sponsor_amount: int = 0  # 建筑数量
seed_amount: int = 0
basket_amount: int = 0
tree_amount: int = 0
garden_amount: int = 0
town_amount: int = 0
country_amount: int = 0
planet_amount: int = 0
wizardtower_amount: int = 0
plane_amount: int = 0
hole_amount: int = 0
timemachine_amount: int = 0
glass_amount: int = 0
js_amount: int = 0

building_amount: int = 0  #　建筑总数量

price_sponsor: int = 10  # 建筑价格
price_seed: int = 80
price_basket: int = 340
price_tree: int = 1500
price_garden: int = 6200
price_town: int = 14000
price_country: int = 89000
price_planet: int = 304000
price_wizardtower: int = 792000
price_plane: int = 1850000
price_hole: int = 4640000
price_timemachine: int = 27000000
price_glass: int = 315000000
price_js: int = 1710000000

value_sponsor: float = 0.5  # 建筑每秒提供苹果数量
value_seed: int = 1
value_basket: int = 3
value_tree: int = 7
value_garden: int = 15
value_town: int = 30
value_country: int = 75
value_planet: int = 110
value_wizardtower: int = 150
value_plane: int = 250
value_hole: int = 400
value_timemachine: int = 750
value_glass: int = 900
value_js: int = 1200

button_clicked_amount_2: int = 0  # 按钮点击次数
button_clicked_amount_3: int = 0
button_clicked_amount_4: int = 0
button_clicked_amount_5: int = 0
button_clicked_amount_6: int = 0
button_clicked_amount_7: int = 0
button_clicked_amount_8: int = 0
button_clicked_amount_9: int = 0
button_clicked_amount_10: int = 0
button_clicked_amount_11: int = 0
button_clicked_amount_12: int = 0
button_clicked_amount_13: int = 0
button_clicked_amount_14: int = 0
button_clicked_amount_15: int = 0

click_time: int = 0  # 点击总次数

upgrade_price: int = 200000  # 升级价格与次数
upgrade_button_clicked_time: int = 0

level_progress_now: int = 1  # 目前等级

difficulty_add_multiply: float = 1.2  # 难度加乘

level_1: int = 800  # 等级划分
level_2: int = 5000
level_3: int = 12000
level_4: int = 60000
level_5: int = 200000
level_6: int = 900000
level_7: int = 5000000
level_8: int = 18000000
level_9: int = 70000000
level_10: int = 250000000
level_11: int = 900000000
level_12: int = 5500000000
level_13: int = 20000000000
level_14: int = 75000000000
level_15: int = 200000000000
level_16: int = 800000000000
level_17: int = 4000000000000
level_18: int = 60000000000000
level_19: int = 200000000000000
level_20: int = 1000000000000000

achievement_1_on: int = 0  # 成就达到要求
achievement_2_on: int = 0
achievement_3_on: int = 0
achievement_4_on: int = 0
achievement_5_on: int = 0
achievement_6_on: int = 0
achievement_7_on: int = 0
achievement_8_on: int = 0
achievement_9_on: int = 0
achievement_10_on: int = 0
achievement_11_on: int = 0
achievement_12_on: int = 0
achievement_13_on: int = 0
achievement_14_on: int = 0
achievement_15_on: int = 0
achievement_16_on: int = 0
achievement_17_on: int = 0
achievement_18_on: int = 0
achievement_19_on: int = 0
achievement_20_on: int = 0
achievement_21_on: int = 0
achievement_22_on: int = 0
achievement_23_on: int = 0
achievement_24_on: int = 0
achievement_25_on: int = 0
achievement_26_on: int = 0
achievement_27_on: int = 0
achievement_28_on: int = 0
achievement_29_on: int = 0
achievement_30_on: int = 0
achievement_31_on: int = 0
achievement_32_on: int = 0
achievement_33_on: int = 0
achievement_34_on: int = 0
achievement_35_on: int = 0
achievement_36_on: int = 0
achievement_37_on: int = 0
achievement_38_on: int = 0
achievement_39_on: int = 0
achievement_40_on: int = 0
achievement_41_on: int = 0
achievement_42_on: int = 0
achievement_43_on: int = 0
achievement_44_on: int = 0
achievement_45_on: int = 0
achievement_46_on: int = 0
achievement_47_on: int = 0
achievement_48_on: int = 0
achievement_49_on: int = 0
achievement_50_on: int = 0
achievement_51_on: int = 0
achievement_52_on: int = 0
achievement_53_on: int = 0
achievement_54_on: int = 0
achievement_55_on: int = 0
achievement_56_on: int = 0
achievement_57_on: int = 0
achievement_58_on: int = 0
achievement_59_on: int = 0
achievement_60_on: int = 0
achievement_60_on: int = 0
achievement_61_on: int = 0
achievement_62_on: int = 0
achievement_63_on: int = 0
achievement_64_on: int = 0
achievement_65_on: int = 0
achievement_66_on: int = 0
achievement_67_on: int = 0
achievement_68_on: int = 0
achievement_69_on: int = 0
achievement_70_on: int = 0
achievement_71_on: int = 0
achievement_72_on: int = 0
achievement_73_on: int = 0
achievement_74_on: int = 0
achievement_75_on: int = 0
achievement_76_on: int = 0
achievement_77_on: int = 0
achievement_78_on: int = 0
achievement_79_on: int = 0
achievement_80_on: int = 0
achievement_81_on: int = 0
achievement_82_on: int = 0
achievement_83_on: int = 0
achievement_84_on: int = 0
achievement_85_on: int = 0

achievement_1_get: int = 0  # 成就获得
achievement_2_get: int = 0
achievement_3_get: int = 0
achievement_4_get: int = 0
achievement_5_get: int = 0
achievement_6_get: int = 0
achievement_7_get: int = 0
achievement_8_get: int = 0
achievement_9_get: int = 0
achievement_10_get: int = 0
achievement_11_get: int = 0
achievement_12_get: int = 0
achievement_13_get: int = 0
achievement_14_get: int = 0
achievement_15_get: int = 0
achievement_16_get: int = 0
achievement_17_get: int = 0
achievement_18_get: int = 0
achievement_19_get: int = 0
achievement_20_get: int = 0
achievement_21_get: int = 0
achievement_22_get: int = 0
achievement_23_get: int = 0
achievement_24_get: int = 0
achievement_25_get: int = 0
achievement_26_get: int = 0
achievement_27_get: int = 0
achievement_28_get: int = 0
achievement_29_get: int = 0
achievement_30_get: int = 0
achievement_31_get: int = 0
achievement_32_get: int = 0
achievement_33_get: int = 0
achievement_34_get: int = 0
achievement_35_get: int = 0
achievement_36_get: int = 0
achievement_37_get: int = 0
achievement_38_get: int = 0
achievement_39_get: int = 0
achievement_40_get: int = 0
achievement_41_get: int = 0
achievement_42_get: int = 0
achievement_43_get: int = 0
achievement_44_get: int = 0
achievement_45_get: int = 0
achievement_46_get: int = 0
achievement_47_get: int = 0
achievement_48_get: int = 0
achievement_49_get: int = 0
achievement_50_get: int = 0
achievement_51_get: int = 0
achievement_52_get: int = 0
achievement_53_get: int = 0
achievement_54_get: int = 0
achievement_55_get: int = 0
achievement_56_get: int = 0
achievement_57_get: int = 0
achievement_58_get: int = 0
achievement_59_get: int = 0
achievement_60_get: int = 0
achievement_61_get: int = 0
achievement_62_get: int = 0
achievement_63_get: int = 0
achievement_64_get: int = 0
achievement_65_get: int = 0
achievement_66_get: int = 0
achievement_67_get: int = 0
achievement_68_get: int = 0
achievement_69_get: int = 0
achievement_70_get: int = 0
achievement_71_get: int = 0
achievement_72_get: int = 0
achievement_73_get: int = 0
achievement_74_get: int = 0
achievement_75_get: int = 0
achievement_76_get: int = 0
achievement_77_get: int = 0
achievement_78_get: int = 0
achievement_79_get: int = 0
achievement_80_get: int = 0
achievement_81_get: int = 0
achievement_82_get: int = 0
achievement_83_get: int = 0
achievement_84_get: int = 0
achievement_85_get: int = 0

music_on: int = 1  # 音效开启

recursion_time: int = 300  # 递归时间

news_all = ['你想种苹果，但没人捧\n场。',  # 新闻
            '你种的第一批苹果被扔\n进了垃圾堆。附近的浣\n熊都避而远之。',
            '你的家人打算试尝一下\n你种的苹果。',
            '你的苹果已经在邻里之\n间小有名气。',
            '大家津津乐道于你的苹\n果。',
            '方圆几里内的人都在讨\n论你的苹果。',
            '你的苹果在整个镇上都\n有了名气！',
            '孩子们都被你的苹果吸\n引了过来。',
            '新闻： 男子抢劫银行，\n只为买苹果。',
            '你的苹果卖出了很多钱。',
            '你的苹果有了自己的专\n题网站。',
            '“我们是优秀的老爷爷。\n”——老爷爷',
            '“乖来亲爷爷一下。”——\n老爷爷',
            '新闻：科学家说化石记\n录表明寒武纪大爆发时\n有苹果基的生物。',
            '一家本地电视台对你的\n苹果进行了长达10分钟\n的新闻报导。你是成功人士了！\n（成功奖励是：一只苹果。）',
            '新闻： 转基因苹果引发\n果农罢工！',
            '新闻： 苹果工厂与全球\n变暖有关！',
            '你的苹果已经畅销海外。\n',
            '“有空给我打电话...”——\n老爷爷',
            '人们跋山涉水只为品尝\n你的苹果。',
            '新闻：苹果工厂罢工——\n工人们要求未来不再使\n用苹果做薪资！',
            '新闻：专家称放养型农\n场苹果在小孩子们中流\n行。',
            '新闻：全苹果菜谱的餐\n厅在市区开张。菜式包\n括红烧苹果、清蒸苹果、\n油炸苹果和苹果片。',
            '新闻：小镇陷入苹果短\n缺，居民被迫吃梨，市\n长承认“还是不太一样”。',
            '新闻：电影因缺少演员\n而被迫取消，导演哀痛\n表示 “每个人都待在家\n狂吃苹果”。',
            '“扭曲吧” ——老爷爷',
            '国王们都喜欢上你的苹\n果了。',
            '“我们会再次升起。” \n——老爷爷',
            '“荒芜吧” ——老爷爷',
            '新闻：时光机被用于非\n法时间旅行！',
            '新闻：“不得不说，苹果\n这东西确实有点不详” \n某些迷糊的白痴如此表示。',
            '“仅仅是一个挫折。” ——\n老爷爷',
            '“侵蚀吧” ——老爷爷',
            '现在有专门为你的苹果\n而开设的博物馆了。',
            '新闻：太空旅游业的蓬\n勃发展为遥远的行星吸引\n了更多无聊的百万富翁！ ',
            '“痛苦吧” ——老爷爷',
            '国际上为你的苹果设立\n了一个纪念日。',
            '新闻：喜剧演员因不相\n关的消化不良而被迫取消\n苹果常规。',
            '“我们没有饱足感。” ——\n老爷爷',
            '新闻：在遥远的星球上\n发现苹果基生物！',
            '“太晚了。” ——老爷爷',
            '新闻：在遥远的星球上\n发现古代的水果文物。”骇\n人听闻的暗示。“科\n学家指出。',
            '新闻：发现新的苹果星\n球，成为苹果贸易飞船的\n目标！',
            '新闻：研究指出工厂制\n造的苹果将导致过胖。',
            '新闻：时光机被卷入全\n城范围内的灾难！',
            '你的苹果被认证为世界\n第八大奇迹。',
            '新闻：苹果农场涉嫌雇\n佣身份不明的老年劳工！',
            '中央决定对你的苹果产\n业进行监控。',
            '新闻：研究指出苹果世\n界传送门会引发快速衰老和\n沉迷于烘焙。',
            '新闻：国民对传送门中\n钻出的奇怪生物表示担忧！',
            '宇宙中的上古神明为了\n尝你的苹果而苏醒。',
            '新闻：大量苹果星球被\n发现有99.8%的正品苹果\n核心！',
            '新闻：新苹果宗教横扫\n全国。',
            '新闻：外国政治家卷入\n苹果走私丑闻',
            '新闻：时光机被用于改\n写历史的阴谋！真的吗？',
            '异次元生物跨越维度来\n品尝你的苹果。',
            '宇宙间所有分子都以苹\n果的形式存在。',
            '“你本来可以制止这一切\n的。”——老爷爷',
            '新闻：科学家说化石记\n录表明寒武纪大爆发时有\n苹果基的生物。',
            '你的苹果已经享誉全球。',
            '外星生物盼望能尝到你\n的苹果。',
            '你的苹果开始拥有了感\n知。',
            '新闻：“我看过了未来，”\n时间机器驾驶员说，“我\n再也不想去那了。”',
            '史册上添加了一整章来\n介绍你的苹果。',
            '新闻：从过去带回来的\n苹果"不适合人类消费"，\n历史学家说。',
            '新闻：神秘的非法苹果\n被缴获，警方表示“味道\n太糟了”。',
            '你的苹果重建了宇宙规\n则。',
            '“不久就该结束了。”——\n老爷爷',
            '新闻： "宇宙中的循环\n太多了，" 研究者说：\n"只有苹果才能解决问题。"',
            '新闻：科学家预言与苹\n果相关的世界末日即将\n到来，成为茶余饭后的笑料。',
            '应该放下游戏了。']

information: str = "欢迎来到 苹果点点乐©!  作者/版权: 轩哥啊哈OvO"  # 初始信息

########## 声音系统 ##########

def achievement_get_sound():  # 获得成就声音
    if music_on == 1:
        pygame.mixer.init()
        pygame.mixer.music.load(r"./sound/Random_levelup.wav")
        pygame.mixer.music.play(start=0.0)
    else:
        pass

def click_sound():  # 按钮点击声音
    if music_on == 1:
        pygame.mixer.init()
        pygame.mixer.music.load(r"./sound/click.wav")
        pygame.mixer.music.play(start=0.0)
    else:
        pass

def pick_apple():  # 获得苹果声音
    if music_on == 1:
        sound_play = random.randint(1,8)
        if sound_play == 1:
            sound_filepath = r"./sound/climb1.wav"
        elif sound_play == 2:
            sound_filepath = r"./sound/climb2.wav"
        elif sound_play == 3:
            sound_filepath = r"./sound/climb3.wav"
        elif sound_play == 4:
            sound_filepath = r"./sound/climb4.wav"
        elif sound_play == 5:
            sound_filepath = r"./sound/climb5.wav"
        elif sound_play == 6:
            sound_filepath = r"./sound/break2.wav"
        elif sound_play == 7:
            sound_filepath = r"./sound/break3.wav"
        elif sound_play == 8:
            sound_filepath = r"./sound/break4.wav"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_filepath)
        pygame.mixer.music.play(start=0.0)
    else:
        pass

def successful_bought_sound():  # 成功购买建筑声音
    if music_on == 1:
        pygame.mixer.init()
        pygame.mixer.music.load(r"./sound/Succesfull_Hit.wav")
        pygame.mixer.music.play(start=0.0)
    else:
        pass

def unsuccessful_bought_sound():  # 未成功购买建筑声音
    if music_on == 1:
        global sound_filepath
        unsuccessful_bought_sound_num= random.randint(1,3)
        if unsuccessful_bought_sound_num == 1:
            sound_filepath = r"./sound/Villager_no1.wav"
        elif unsuccessful_bought_sound_num == 2:
            sound_filepath = r"./sound/Villager_no2.wav"
        elif unsuccessful_bought_sound_num == 3:
            sound_filepath = r"./sound/Villager_no3.wav"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_filepath)
        pygame.mixer.music.play(start=0.0)
    else:
        pass

########## 内部用法 ##########

def get_news():
    news = []
    if apple_amount_total == 0: 
        for news_num in range(0,1): news.append(news_all[news_num])
    elif apple_amount_total < 30: 
        for news_num in range(1,3): news.append(news_all[news_num])
    elif apple_amount_total < 100: 
        for news_num in range(1,4): news.append(news_all[news_num])
    elif apple_amount_total < 300: 
        for news_num in range(1,6): news.append(news_all[news_num])
    elif apple_amount_total < 700: 
        for news_num in range(6,8): news.append(news_all[news_num])
    elif apple_amount_total < 1500: 
        for news_num in range(6,10): news.append(news_all[news_num])
    elif apple_amount_total < 3000: 
        for news_num in range(6,12): news.append(news_all[news_num])
    elif apple_amount_total < 5000: 
        for news_num in range(13,30): news.append(news_all[news_num])
    elif apple_amount_total < 8000: 
        for news_num in range(13,35): news.append(news_all[news_num])
    elif apple_amount_total < 10000: 
        for news_num in range(13,40): news.append(news_all[news_num])
    elif apple_amount_total < 30000: 
        for news_num in range(13,45): news.append(news_all[news_num])
    elif apple_amount_total < 50000: 
        for news_num in range(13,50): news.append(news_all[news_num])
    elif apple_amount_total < 80000: 
        for news_num in range(13,55): news.append(news_all[news_num])
    elif apple_amount_total < 100000: 
        for news_num in range(13,60): news.append(news_all[news_num])
    elif apple_amount_total < 500000: 
        for news_num in range(13,65): news.append(news_all[news_num])
    elif apple_amount_total < 1000000: 
        for news_num in range(13,70): news.append(news_all[news_num])
    return news

########## 按钮点击运算 ##########

def click_button_clicked():  # 苹果按钮点击运算
    global apple_amount, apple_amount_total, click_time
    pick_apple()
    apple_amount += add_per_click
    apple_amount_total += add_per_click
    click_time += 1

def sponsor_button_clicked():  # 建筑购买运算
    global apple_amount, price_sponsor, sponsor_amount, information, button_clicked_amount_2
    if (apple_amount - price_sponsor) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_sponsor) + " 个苹果 以购买 鼠标指针。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 鼠标指针。"
        successful_bought_sound()
        apple_amount -= price_sponsor
        button_clicked_amount_2 += 1
        price_sponsor += button_clicked_amount_2
        sponsor_amount += 1

def seed_button_clicked():
    global apple_amount, price_seed, seed_amount, information, button_clicked_amount_3
    if (apple_amount - price_seed) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_seed) + " 个苹果 以购买 果篮。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 果篮。"
        successful_bought_sound()
        apple_amount -= price_seed
        button_clicked_amount_3 += 1
        price_seed += button_clicked_amount_3 * 2
        seed_amount += 1

def basket_button_clicked():
    global apple_amount, price_basket, basket_amount, information, button_clicked_amount_4
    if (apple_amount - price_basket) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_basket) + " 个苹果 以购买 老爷爷。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 老爷爷。"
        successful_bought_sound()
        apple_amount -= price_basket
        button_clicked_amount_4 += 1
        price_basket += button_clicked_amount_4 * 3
        basket_amount += 1

def tree_button_clicked():
    global apple_amount, price_tree, tree_amount, information, button_clicked_amount_5
    if (apple_amount - price_tree) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_tree) + " 个苹果 以购买 苹果树。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 苹果树。"
        successful_bought_sound()
        apple_amount -= price_tree
        button_clicked_amount_5 += 1
        price_tree += button_clicked_amount_5 * 4
        tree_amount += 1

def garden_button_clicked():
    global apple_amount, price_garden, garden_amount, information, button_clicked_amount_6
    if (apple_amount - price_garden) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_garden) + " 个苹果 以购买 果园。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 果园。"
        successful_bought_sound()
        apple_amount -= price_garden
        button_clicked_amount_6 += 1
        price_garden += button_clicked_amount_6 * 5
        garden_amount += 1

def town_button_clicked():
    global apple_amount, price_town, town_amount, information, button_clicked_amount_7
    if (apple_amount - price_town) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_town) + " 个苹果 以购买 水果镇。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 水果镇。"
        successful_bought_sound()
        apple_amount -= price_town
        button_clicked_amount_7 += 1
        price_town += button_clicked_amount_7 * 6
        town_amount += 1

def country_button_clicked():
    global apple_amount, price_country, country_amount, information, button_clicked_amount_8
    if (apple_amount - price_country) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_country) + " 个苹果 以购买 苹果工厂。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 苹果工厂。"
        successful_bought_sound()
        apple_amount -= price_country
        button_clicked_amount_8 += 1
        price_country += button_clicked_amount_8 * 7
        country_amount += 1

def planet_button_clicked():
    global apple_amount, price_planet, planet_amount, information, button_clicked_amount_9
    if (apple_amount - price_planet) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_planet) + " 个苹果 以购买 水果银行。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 水果银行。"
        successful_bought_sound()
        apple_amount -= price_planet
        button_clicked_amount_9 += 1
        price_planet += button_clicked_amount_9 * 8
        planet_amount += 1

def wizardtower_button_clicked():
    global apple_amount, price_wizardtower, wizardtower_amount, information, button_clicked_amount_10
    if (apple_amount - price_wizardtower) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_wizardtower) + " 个苹果 以购买 魔法巫师塔。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 魔法巫师塔。"
        successful_bought_sound()
        apple_amount -= price_wizardtower
        button_clicked_amount_10 += 1
        price_wizardtower += button_clicked_amount_10 * 9
        wizardtower_amount += 1

def plane_button_clicked():
    global apple_amount, price_plane, plane_amount, information, button_clicked_amount_11
    if (apple_amount - price_plane) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_plane) + " 个苹果 以购买 宇宙飞船。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 宇宙飞船。"
        successful_bought_sound()
        apple_amount -= price_plane
        button_clicked_amount_11 += 1
        price_plane += button_clicked_amount_11 * 10
        plane_amount += 1

def hole_button_clicked():
    global apple_amount, price_hole, hole_amount, information, button_clicked_amount_12
    if (apple_amount - price_hole) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_hole) + " 个苹果 以购买 虫洞。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 虫洞。"
        successful_bought_sound()
        apple_amount -= price_hole
        button_clicked_amount_12 += 1
        price_hole += button_clicked_amount_12 * 11
        hole_amount += 1

def timemachine_button_clicked():
    global apple_amount, price_timemachine, timemachine_amount, information, button_clicked_amount_13
    if (apple_amount - price_timemachine) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_timemachine) + " 个苹果 以购买 时光机。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 时光机。"
        successful_bought_sound()
        apple_amount -= price_timemachine
        button_clicked_amount_13 += 1
        price_timemachine += button_clicked_amount_13 * 12
        timemachine_amount += 1

def glass_button_clicked():
    global apple_amount, price_glass, glass_amount, information, button_clicked_amount_14
    if (apple_amount - price_glass) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_glass) + " 个苹果 以购买 三棱镜。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 三棱镜。"
        successful_bought_sound()
        apple_amount -= price_glass
        button_clicked_amount_14 += 1
        price_glass += button_clicked_amount_14 * 13
        glass_amount += 1

def js_button_clicked():
    global apple_amount, price_js, js_amount, information, button_clicked_amount_15
    if (apple_amount - price_js) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_js) + " 个苹果 以购买 Python 控制台。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 Python 控制台。"
        successful_bought_sound()
        apple_amount -= price_js
        button_clicked_amount_15 += 1
        price_js += button_clicked_amount_15 * 14
        js_amount += 1

def upgrade_button_clicked():  # 升级运算
    global apple_amount, information, upgrade_button_clicked_time
    if (apple_amount - upgrade_price) < 0:
        unsuccessful_bought_sound()
        information = "没有足够的苹果。你需要至少 " + str(int(upgrade_price)) + " 个苹果以升级。"
    else:
        successful_bought_sound()
        apple_amount -= upgrade_price
        upgrade_button_clicked_time += 1
        information = "你升级至了 Level " + str(upgrade_button_clicked_time + 1) + "！"

def refresh_newspaper():  # 报纸刷新
    global newspaper
    newspaper['text'] = "报纸\n\n"+get_news()[random.randint(0,len(get_news())-1)]

########## 递归显示运算 ##########

def apple_amount_entry_update():  # 左侧信息栏显示递归
    global apple_amount, add_per_click, auto_add_per_second
    apple_amount_entry.delete(0, "end")
    apple_amount_entry.insert(0, str(apple_amount))
    apple_per_click_entry.delete(0, "end")
    apple_per_click_entry.insert(0, ("+ " + str(add_per_click) + " / click"))
    apple_per_second_entry.delete(0, "end")
    apple_per_second_entry.insert(0, ("+ " + str(auto_add_per_second) + " / s"))
    apple_amount_entry.after(100, apple_amount_entry_update)

def entry_information_number_upgrade():  # 信息网格显示递归
    global sponsor_amount, seed_amount, basket_amount, tree_amount, garden_amount
    global town_amount, country_amount, planet_amount, wizardtower_amount, plane_amount
    global hole_amount, timemachine_amount, glass_amount, js_amount
    entry_information_number_23.delete(0, "end")
    entry_information_number_23.insert(0, str(sponsor_amount))
    entry_information_number_33.delete(0, "end")
    entry_information_number_33.insert(0, str(seed_amount))
    entry_information_number_43.delete(0, "end")
    entry_information_number_43.insert(0, str(basket_amount))
    entry_information_number_53.delete(0, "end")
    entry_information_number_53.insert(0, str(tree_amount))
    entry_information_number_63.delete(0, "end")
    entry_information_number_63.insert(0, str(garden_amount))
    entry_information_number_73.delete(0, "end")
    entry_information_number_73.insert(0, str(town_amount))
    entry_information_number_83.delete(0, "end")
    entry_information_number_83.insert(0, str(country_amount))
    entry_information_number_93.delete(0, "end")
    entry_information_number_93.insert(0, str(planet_amount))
    entry_information_number_103.delete(0, "end")
    entry_information_number_103.insert(0, str(wizardtower_amount))
    entry_information_number_113.delete(0, "end")
    entry_information_number_113.insert(0, str(plane_amount))
    entry_information_number_123.delete(0, "end")
    entry_information_number_123.insert(0, str(hole_amount))
    entry_information_number_133.delete(0, "end")
    entry_information_number_133.insert(0, str(timemachine_amount))
    entry_information_number_143.delete(0, "end")
    entry_information_number_143.insert(0, str(glass_amount))
    entry_information_number_153.delete(0, "end")
    entry_information_number_153.insert(0, str(js_amount))

    global price_sponsor, price_seed, price_basket, price_tree, price_garden
    global price_town, price_country, price_planet, price_wizardtower, price_plane
    global price_hole, price_timemachine, price_glass, price_js
    entry_information_number_24.delete(0, "end")
    entry_information_number_24.insert(0, str(price_sponsor))
    entry_information_number_34.delete(0, "end")
    entry_information_number_34.insert(0, str(price_seed))
    entry_information_number_44.delete(0, "end")
    entry_information_number_44.insert(0, str(price_basket))
    entry_information_number_54.delete(0, "end")
    entry_information_number_54.insert(0, str(price_tree))
    entry_information_number_64.delete(0, "end")
    entry_information_number_64.insert(0, str(price_garden))
    entry_information_number_74.delete(0, "end")
    entry_information_number_74.insert(0, str(price_town))
    entry_information_number_84.delete(0, "end")
    entry_information_number_84.insert(0, str(price_country))
    entry_information_number_94.delete(0, "end")
    entry_information_number_94.insert(0, str(price_planet))
    entry_information_number_104.delete(0, "end")
    entry_information_number_104.insert(0, str(price_wizardtower))
    entry_information_number_114.delete(0, "end")
    entry_information_number_114.insert(0, str(price_plane))
    entry_information_number_124.delete(0, "end")
    entry_information_number_124.insert(0, str(price_hole))
    entry_information_number_134.delete(0, "end")
    entry_information_number_134.insert(0, str(price_timemachine))
    entry_information_number_144.delete(0, "end")
    entry_information_number_144.insert(0, str(price_glass))
    entry_information_number_154.delete(0, "end")
    entry_information_number_154.insert(0, str(price_js))

    global value_sponsor, value_seed, value_basket, value_tree, value_garden
    global value_hole, value_timemachine, value_glass, value_js
    global value_town, value_country, value_planet, value_wizardtower, value_plane
    entry_information_number_30.delete(0, "end")
    entry_information_number_30.insert(0, ("+" + str(value_sponsor * sponsor_amount)) + " / s")
    entry_information_number_35.delete(0, "end")
    entry_information_number_35.insert(0, ("+" + str(value_seed * seed_amount)) + " / s")
    entry_information_number_45.delete(0, "end")
    entry_information_number_45.insert(0, ("+" + str(value_basket * basket_amount)) + " / s")
    entry_information_number_55.delete(0, "end")
    entry_information_number_55.insert(0, ("+" + str(value_tree * tree_amount)) + " / s")
    entry_information_number_65.delete(0, "end")
    entry_information_number_65.insert(0, ("+" + str(value_garden * garden_amount)) + " / s")
    entry_information_number_75.delete(0, "end")
    entry_information_number_75.insert(0, ("+" + str(value_town * town_amount)) + " / s")
    entry_information_number_85.delete(0, "end")
    entry_information_number_85.insert(0, ("+" + str(value_country * country_amount)) + " / s")
    entry_information_number_95.delete(0, "end")
    entry_information_number_95.insert(0, ("+" + str(value_planet * planet_amount)) + " / s")
    entry_information_number_105.delete(0, "end")
    entry_information_number_105.insert(0, ("+" + str(value_wizardtower * wizardtower_amount)) + " / s")
    entry_information_number_115.delete(0, "end")
    entry_information_number_115.insert(0, ("+" + str(value_plane * plane_amount)) + " / s")
    entry_information_number_130.delete(0, "end")
    entry_information_number_130.insert(0, ("+" + str(value_hole * hole_amount)) + " / s")
    entry_information_number_135.delete(0, "end")
    entry_information_number_135.insert(0, ("+" + str(value_timemachine * timemachine_amount)) + " / s")
    entry_information_number_145.delete(0, "end")
    entry_information_number_145.insert(0, ("+" + str(value_glass * glass_amount)) + " / s")
    entry_information_number_155.delete(0, "end")
    entry_information_number_155.insert(0, ("+" + str(value_js * js_amount)) + " / s")
    entry_information_number_155.after(recursion_time, entry_information_number_upgrade)

def entry_information_information_upgrade():  # 信息栏显示递归
    entry_information_information.delete(0, "end")
    entry_information_information.insert(0, information)
    entry_information_information.after(recursion_time, entry_information_information_upgrade)

def statistics_text_upgrade():  # 统计信息显示递归
    statistics_text.delete(1.0, tk.END)
    statistics_text.insert("insert", ("现在的苹果数量：" + str(apple_amount) +
                                      "\n总苹果数量：" + str(apple_amount_total) +
                                      "\n总建筑数量：" + str(building_amount) +
                                      "\n点击次数：" + str(click_time)))
    statistics_text.after(recursion_time, statistics_text_upgrade)

def upgrade_button_entry_update():  # 升级显示递归
    upgrade_button_entry.delete(0, "end")
    upgrade_button_entry.insert(0, "Level " + str(upgrade_button_clicked_time + 1) + " 至 Level " + str(upgrade_button_clicked_time + 2))
    upgrade_button_entry_price.delete(0, "end")
    upgrade_button_entry_price.insert(0, "价格：" + str(int(upgrade_price)))
    upgrade_button_entry.after(recursion_time, upgrade_button_entry_update)

def achievement_progress_update():  # 成就进度条显示递归
    achievement_get_num = (achievement_1_get + achievement_2_get + achievement_3_get + achievement_4_get + achievement_5_get + 
                          achievement_6_get + achievement_7_get + achievement_8_get + achievement_9_get + achievement_10_get + 
                          achievement_11_get + achievement_12_get + achievement_13_get + achievement_14_get + achievement_15_get + 
                          achievement_16_get + achievement_17_get + achievement_18_get + achievement_19_get + achievement_20_get + 
                          achievement_21_get + achievement_22_get + achievement_23_get + achievement_24_get + achievement_25_get + 
                          achievement_26_get + achievement_27_get + achievement_28_get + achievement_29_get + achievement_30_get + 
                          achievement_31_get + achievement_32_get + achievement_33_get + achievement_34_get + achievement_35_get + 
                          achievement_36_get + achievement_37_get + achievement_38_get + achievement_39_get + achievement_40_get + 
                          achievement_41_get + achievement_42_get + achievement_43_get + achievement_44_get + achievement_45_get + 
                          achievement_46_get + achievement_47_get + achievement_48_get + achievement_49_get + achievement_50_get + 
                          achievement_51_get + achievement_52_get + achievement_53_get + achievement_54_get + achievement_55_get + 
                          achievement_56_get + achievement_57_get + achievement_58_get + achievement_59_get + achievement_60_get + 
                          achievement_61_get + achievement_62_get + achievement_63_get + achievement_64_get + achievement_65_get + 
                          achievement_66_get + achievement_67_get + achievement_68_get + achievement_69_get + achievement_70_get + 
                          achievement_71_get + achievement_72_get + achievement_73_get + achievement_74_get + achievement_75_get + 
                          achievement_76_get + achievement_77_get + achievement_78_get + achievement_79_get + achievement_80_get + 
                          achievement_81_get + achievement_82_get + achievement_83_get + achievement_84_get + achievement_85_get)
    achievement_progress_bar['value'] = achievement_get_num
    achievement_progress_entry.delete(0, "end")
    achievement_progress_entry.insert(0, str(achievement_get_num) + "/" + str(achevement_num_all))
    achievement_progress_entry.after(recursion_time, achievement_progress_update)

def time_entry_update():  # 时间显示递归
    time_entry.delete(0, "end")
    time_entry.insert(0, time.asctime(time.localtime(time.time())))
    time_entry.after(300, time_entry_update)

def level_progress_bar_update():  # 等级进度条显示递归
    if level_progress_now == 1: level_progress_bar['maximum'] = level_1; level_progress_bar['value'] = apple_amount_total
    elif level_progress_now == 2: level_progress_bar['maximum'] = level_2 - level_1; level_progress_bar['value'] = apple_amount_total - level_1
    elif level_progress_now == 3: level_progress_bar['maximum'] = level_3 - level_2; level_progress_bar['value'] = apple_amount_total - level_2
    elif level_progress_now == 4: level_progress_bar['maximum'] = level_4 - level_3; level_progress_bar['value'] = apple_amount_total - level_3
    elif level_progress_now == 5: level_progress_bar['maximum'] = level_5 - level_4; level_progress_bar['value'] = apple_amount_total - level_4
    elif level_progress_now == 6: level_progress_bar['maximum'] = level_6 - level_5; level_progress_bar['value'] = apple_amount_total - level_5
    elif level_progress_now == 7: level_progress_bar['maximum'] = level_7 - level_6; level_progress_bar['value'] = apple_amount_total - level_6
    elif level_progress_now == 8: level_progress_bar['maximum'] = level_8 - level_7; level_progress_bar['value'] = apple_amount_total - level_7
    elif level_progress_now == 9: level_progress_bar['maximum'] = level_9 - level_8; level_progress_bar['value'] = apple_amount_total - level_8
    elif level_progress_now == 10: level_progress_bar['maximum'] = level_10 - level_9; level_progress_bar['value'] = apple_amount_total - level_9
    elif level_progress_now == 11: level_progress_bar['maximum'] = level_11 - level_10; level_progress_bar['value'] = apple_amount_total - level_10
    elif level_progress_now == 12: level_progress_bar['maximum'] = level_12 - level_11; level_progress_bar['value'] = apple_amount_total - level_11
    elif level_progress_now == 13: level_progress_bar['maximum'] = level_13 - level_12; level_progress_bar['value'] = apple_amount_total - level_12
    elif level_progress_now == 14: level_progress_bar['maximum'] = level_14 - level_13; level_progress_bar['value'] = apple_amount_total - level_13
    elif level_progress_now == 15: level_progress_bar['maximum'] = level_15 - level_14; level_progress_bar['value'] = apple_amount_total - level_14
    elif level_progress_now == 16: level_progress_bar['maximum'] = level_16 - level_15; level_progress_bar['value'] = apple_amount_total - level_15
    elif level_progress_now == 17: level_progress_bar['maximum'] = level_17 - level_16; level_progress_bar['value'] = apple_amount_total - level_16
    elif level_progress_now == 18: level_progress_bar['maximum'] = level_18 - level_17; level_progress_bar['value'] = apple_amount_total - level_17
    elif level_progress_now == 19: level_progress_bar['maximum'] = level_19 - level_18; level_progress_bar['value'] = apple_amount_total - level_18
    elif level_progress_now == 20: level_progress_bar['maximum'] = level_20 - level_19; level_progress_bar['value'] = apple_amount_total - level_19
    level_progress_label_left.delete(0, "end")
    level_progress_label_left.insert(0, "Level " + str(level_progress_now))
    level_progress_label_right.delete(0, "end")
    level_progress_label_right.insert(0, "Level " + str(level_progress_now + 1))
    level_progress_bar.after(recursion_time, level_progress_bar_update)

########## 逻辑运算线程 ##########

def main_operation_logic():  # 主要运算逻辑线程
    global apple_amount, apple_amount_total, building_amount, auto_add_per_second, add_per_click
    while True:
        auto_add_per_second = int(((sponsor_amount * value_sponsor) +
                                   (seed_amount * value_seed) +
                                   (basket_amount * value_basket) +
                                   (tree_amount * value_tree) +
                                   (garden_amount * value_garden) +
                                   (town_amount * value_town) +
                                   (country_amount * value_country) +
                                   (planet_amount * value_planet) +
                                   (wizardtower_amount * value_wizardtower) +
                                   (plane_amount * value_plane) +
                                   (hole_amount * value_hole) +
                                   (timemachine_amount * value_timemachine) +
                                   (glass_amount * value_glass) +
                                   (js_amount * value_js)) * pow(1.03, upgrade_button_clicked_time + 1))
        apple_amount += auto_add_per_second
        apple_amount_total += auto_add_per_second
        add_per_click = int((sponsor_amount * 0.5) + \
                            (seed_amount * 0.5) + \
                            (basket_amount * 0.5) + \
                            (tree_amount * 1) + \
                            (garden_amount * 1) + \
                            (town_amount * 1.5) + \
                            (country_amount * 1.5) + \
                            (planet_amount * 2) + \
                            (wizardtower_amount * 2) + \
                            (plane_amount * 2.5) + \
                            (hole_amount * 2.5) + \
                            (timemachine_amount * 3) + \
                            (glass_amount * 4) + \
                            (js_amount * 5))
        if add_per_click == 0: add_per_click = 1
        building_amount = (sponsor_amount + seed_amount + basket_amount + tree_amount + garden_amount + 
                          town_amount + country_amount + planet_amount + wizardtower_amount + 
                          plane_amount + hole_amount + timemachine_amount + glass_amount + js_amount)
        time.sleep(1)

def upgrade_price_logic():  # 升级价格逻辑线程
    global upgrade_price
    while True:
        upgrade_price = int(200000 * pow(1.2, upgrade_button_clicked_time))
        time.sleep(1)

def progress_bar_logic():  # 进度条逻辑线程
    global level_progress_now
    while True:
        if apple_amount_total < level_1:
            level_progress_now = 1
        elif apple_amount_total < level_2:
            level_progress_now = 2
        elif apple_amount_total < level_3:
            level_progress_now = 3
        elif apple_amount_total < level_4:
            level_progress_now = 4
        elif apple_amount_total < level_5:
            level_progress_now = 5
        elif apple_amount_total < level_6:
            level_progress_now = 6
        elif apple_amount_total < level_7:
            level_progress_now = 7
        elif apple_amount_total < level_8:
            level_progress_now = 8
        elif apple_amount_total < level_9:
            level_progress_now = 9
        elif apple_amount_total < level_10:
            level_progress_now = 10
        elif apple_amount_total < level_11:
            level_progress_now = 11
        elif apple_amount_total < level_12:
            level_progress_now = 12
        elif apple_amount_total < level_13:
            level_progress_now = 13
        elif apple_amount_total < level_14:
            level_progress_now = 14
        elif apple_amount_total < level_15:
            level_progress_now = 15
        elif apple_amount_total < level_16:
            level_progress_now = 16
        elif apple_amount_total < level_17:
            level_progress_now = 17
        elif apple_amount_total < level_18:
            level_progress_now = 18
        elif apple_amount_total < level_19:
            level_progress_now = 19
        elif apple_amount_total < level_20:
            level_progress_now = 20
        else:
            level_progress_now = 21
        time.sleep(1)

def achievement_logic():  # 成就逻辑线程
    global information
    global achievement_1_get, achievement_2_get, achievement_3_get, achievement_4_get, achievement_5_get
    global achievement_6_get, achievement_7_get, achievement_8_get, achievement_9_get, achievement_10_get
    global achievement_11_get, achievement_12_get, achievement_13_get, achievement_14_get, achievement_15_get
    global achievement_16_get, achievement_17_get, achievement_18_get, achievement_19_get, achievement_20_get
    global achievement_21_get, achievement_22_get, achievement_23_get, achievement_24_get, achievement_25_get
    global achievement_26_get, achievement_27_get, achievement_28_get, achievement_29_get, achievement_30_get
    global achievement_31_get, achievement_32_get, achievement_33_get, achievement_34_get, achievement_35_get
    global achievement_36_get, achievement_37_get, achievement_38_get, achievement_39_get, achievement_40_get
    global achievement_41_get, achievement_42_get, achievement_43_get, achievement_44_get, achievement_45_get
    global achievement_46_get, achievement_47_get, achievement_48_get, achievement_49_get, achievement_50_get
    global achievement_51_get, achievement_52_get, achievement_53_get, achievement_54_get, achievement_55_get
    global achievement_56_get, achievement_57_get, achievement_58_get, achievement_59_get, achievement_60_get
    global achievement_61_get, achievement_62_get, achievement_63_get, achievement_64_get, achievement_65_get
    global achievement_66_get, achievement_67_get, achievement_68_get, achievement_69_get, achievement_70_get
    global achievement_71_get, achievement_72_get, achievement_73_get, achievement_74_get, achievement_75_get
    global achievement_76_get, achievement_77_get, achievement_78_get, achievement_79_get, achievement_80_get
    global achievement_81_get, achievement_82_get, achievement_83_get, achievement_84_get, achievement_85_get
    
    achievement = ToastNotifier()

    def achievement_get(title,rule):
        global information
        information = "恭喜你 获得成就 ["+title+"]："+rule+"！"
        achievement_get_sound()
        toast_title = "获得成就 ["+title+"]"
        achievements_information_text.insert(tk.END, toast_title + ": " + rule + "\n")
        achievement.show_toast(title=toast_title, msg=rule, icon_path="./assets/app16x16.ico", duration=5)

    while True:
        achievement_1_on = 1 if apple_amount >= 1 and achievement_1_get == 0 else 0
        achievement_2_on = 1 if apple_amount >= 100 and achievement_2_get == 0 else 0
        achievement_3_on = 1 if apple_amount >= 1000 and achievement_3_get == 0 else 0
        achievement_4_on = 1 if apple_amount >= 10000 and achievement_4_get == 0 else 0
        achievement_5_on = 1 if apple_amount >= 100000 and achievement_5_get == 0 else 0
        achievement_6_on = 1 if apple_amount >= 1000000 and achievement_6_get == 0 else 0
        achievement_7_on = 1 if apple_amount >= 10000000 and achievement_7_get == 0 else 0
        achievement_8_on = 1 if apple_amount >= 100000000 and achievement_8_get == 0 else 0
        achievement_9_on = 1 if apple_amount >= 1000000000 and achievement_9_get == 0 else 0
        achievement_10_on = 1 if apple_amount >= 10000000000 and achievement_10_get == 0 else 0
        achievement_31_on = 1 if apple_amount >= 100000000000 and achievement_31_get == 0 else 0
        achievement_32_on = 1 if apple_amount >= 1000000000000 and achievement_32_get == 0 else 0
        achievement_33_on = 1 if apple_amount >= 10000000000000 and achievement_33_get == 0 else 0
        achievement_34_on = 1 if apple_amount >= 100000000000000 and achievement_34_get == 0 else 0
        achievement_35_on = 1 if apple_amount >= 1000000000000000 and achievement_35_get == 0 else 0

        achievement_11_on = 1 if sponsor_amount >= 1 and achievement_11_get == 0 else 0
        achievement_12_on = 1 if sponsor_amount >= 2 and achievement_12_get == 0 else 0
        achievement_13_on = 1 if sponsor_amount >= 10 and achievement_13_get == 0 else 0
        achievement_14_on = 1 if sponsor_amount >= 50 and achievement_14_get == 0 else 0
        achievement_15_on = 1 if sponsor_amount >= 100 and achievement_15_get == 0 else 0

        achievement_16_on = 1 if seed_amount >= 1 and achievement_16_get == 0 else 0
        achievement_17_on = 1 if seed_amount >= 5 and achievement_17_get == 0 else 0
        achievement_18_on = 1 if seed_amount >= 10 and achievement_18_get == 0 else 0
        achievement_19_on = 1 if seed_amount >= 50 and achievement_19_get == 0 else 0
        achievement_20_on = 1 if seed_amount >= 100 and achievement_20_get == 0 else 0

        achievement_21_on = 1 if basket_amount >= 1 and achievement_21_get == 0 else 0
        achievement_22_on = 1 if basket_amount >= 5 and achievement_22_get == 0 else 0
        achievement_23_on = 1 if basket_amount >= 10 and achievement_23_get == 0 else 0
        achievement_24_on = 1 if basket_amount >= 50 and achievement_24_get == 0 else 0
        achievement_25_on = 1 if basket_amount >= 100 and achievement_25_get == 0 else 0
            
        achievement_26_on = 1 if tree_amount >= 1 and achievement_26_get == 0 else 0
        achievement_27_on = 1 if tree_amount >= 5 and achievement_27_get == 0 else 0
        achievement_28_on = 1 if tree_amount >= 10 and achievement_28_get == 0 else 0
        achievement_29_on = 1 if tree_amount >= 50 and achievement_29_get == 0 else 0
        achievement_30_on = 1 if tree_amount >= 100 and achievement_30_get == 0 else 0
            
        achievement_36_on = 1 if garden_amount >= 1 and achievement_36_get == 0 else 0
        achievement_37_on = 1 if garden_amount >= 5 and achievement_37_get == 0 else 0
        achievement_38_on = 1 if garden_amount >= 10 and achievement_38_get == 0 else 0
        achievement_39_on = 1 if garden_amount >= 50 and achievement_39_get == 0 else 0
        achievement_40_on = 1 if garden_amount >= 100 and achievement_40_get == 0 else 0
        
        achievement_41_on = 1 if town_amount >= 1 and achievement_41_get == 0 else 0
        achievement_42_on = 1 if town_amount >= 5 and achievement_42_get == 0 else 0
        achievement_43_on = 1 if town_amount >= 10 and achievement_43_get == 0 else 0
        achievement_44_on = 1 if town_amount >= 50 and achievement_44_get == 0 else 0
        achievement_45_on = 1 if town_amount >= 100 and achievement_45_get == 0 else 0

        achievement_46_on = 1 if country_amount >= 1 and achievement_46_get == 0 else 0
        achievement_47_on = 1 if country_amount >= 5 and achievement_47_get == 0 else 0
        achievement_48_on = 1 if country_amount >= 10 and achievement_48_get == 0 else 0
        achievement_49_on = 1 if country_amount >= 50 and achievement_49_get == 0 else 0
        achievement_50_on = 1 if country_amount >= 100 and achievement_50_get == 0 else 0

        achievement_51_on = 1 if planet_amount >= 1 and achievement_51_get == 0 else 0
        achievement_52_on = 1 if planet_amount >= 5 and achievement_52_get == 0 else 0
        achievement_53_on = 1 if planet_amount >= 10 and achievement_53_get == 0 else 0
        achievement_54_on = 1 if planet_amount >= 50 and achievement_54_get == 0 else 0
        achievement_55_on = 1 if planet_amount >= 100 and achievement_55_get == 0 else 0

        achievement_56_on = 1 if wizardtower_amount >= 1 and achievement_56_get == 0 else 0
        achievement_57_on = 1 if wizardtower_amount >= 5 and achievement_57_get == 0 else 0
        achievement_58_on = 1 if wizardtower_amount >= 10 and achievement_58_get == 0 else 0
        achievement_59_on = 1 if wizardtower_amount >= 50 and achievement_59_get == 0 else 0
        achievement_60_on = 1 if wizardtower_amount >= 100 and achievement_60_get == 0 else 0        

        achievement_61_on = 1 if plane_amount >= 1 and achievement_61_get == 0 else 0
        achievement_62_on = 1 if plane_amount >= 5 and achievement_62_get == 0 else 0
        achievement_63_on = 1 if plane_amount >= 10 and achievement_63_get == 0 else 0
        achievement_64_on = 1 if plane_amount >= 50 and achievement_64_get == 0 else 0
        achievement_65_on = 1 if plane_amount >= 100 and achievement_65_get == 0 else 0

        achievement_66_on = 1 if hole_amount >= 1 and achievement_66_get == 0 else 0
        achievement_67_on = 1 if hole_amount >= 5 and achievement_67_get == 0 else 0
        achievement_68_on = 1 if hole_amount >= 10 and achievement_68_get == 0 else 0
        achievement_69_on = 1 if hole_amount >= 50 and achievement_69_get == 0 else 0
        achievement_70_on = 1 if hole_amount >= 100 and achievement_70_get == 0 else 0

        achievement_71_on = 1 if timemachine_amount >= 1 and achievement_71_get == 0 else 0
        achievement_72_on = 1 if timemachine_amount >= 5 and achievement_72_get == 0 else 0
        achievement_73_on = 1 if timemachine_amount >= 10 and achievement_73_get == 0 else 0
        achievement_74_on = 1 if timemachine_amount >= 50 and achievement_74_get == 0 else 0
        achievement_75_on = 1 if timemachine_amount >= 100 and achievement_75_get == 0 else 0

        achievement_76_on = 1 if glass_amount >= 1 and achievement_76_get == 0 else 0
        achievement_77_on = 1 if glass_amount >= 5 and achievement_77_get == 0 else 0
        achievement_78_on = 1 if glass_amount >= 10 and achievement_78_get == 0 else 0
        achievement_79_on = 1 if glass_amount >= 50 and achievement_79_get == 0 else 0
        achievement_80_on = 1 if glass_amount >= 100 and achievement_80_get == 0 else 0

        achievement_81_on = 1 if js_amount >= 1 and achievement_81_get == 0 else 0
        achievement_82_on = 1 if js_amount >= 5 and achievement_82_get == 0 else 0
        achievement_83_on = 1 if js_amount >= 10 and achievement_83_get == 0 else 0
        achievement_84_on = 1 if js_amount >= 50 and achievement_84_get == 0 else 0
        achievement_85_on = 1 if js_amount >= 100 and achievement_85_get == 0 else 0

        if achievement_1_on == 1: achievement_1_get = 1; achievement_get("春天的苏醒","收获 1 个苹果")
        if achievement_2_on == 1: achievement_2_get = 1; achievement_get("苹果的气息", "收获 100 个苹果")
        if achievement_3_on == 1: achievement_3_get = 1; achievement_get("富足果园", "收获 1000 个苹果")
        if achievement_4_on == 1: achievement_4_get = 1; achievement_get("知名果园", "收获 10000 个苹果")
        if achievement_5_on == 1: achievement_5_get = 1; achievement_get("现在别阻止我", "收获 100000 个苹果")
        if achievement_6_on == 1: achievement_6_get = 1; achievement_get("我需要大一点的果园", "收获 1000000 个苹果")
        if achievement_7_on == 1: achievement_7_get = 1; achievement_get("我这么做是为了什么？", "收获 10000000 个苹果")
        if achievement_8_on == 1: achievement_8_get = 1; achievement_get("你要全吃了吗？", "收获 100000000 个苹果")
        if achievement_9_on == 1: achievement_9_get = 1; achievement_get("得苹果者，得宇宙", "收获 1000000000 个苹果")
        if achievement_10_on == 1: achievement_10_get = 1; achievement_get("我做过最棒的梦", "收获 10000000000 个苹果")
        if achievement_31_on == 1: achievement_31_get = 1; achievement_get("我只是随便点一点", "收获 100000000000 个苹果")
        if achievement_32_on == 1: achievement_32_get = 1; achievement_get("你还很饿", "收获 1000000000000 个苹果")
        if achievement_33_on == 1: achievement_33_get = 1; achievement_get("最大容量", "收获 10000000000000 个苹果")
        if achievement_34_on == 1: achievement_34_get = 1; achievement_get("假装，直到你摘下一颗苹果", "收获 100000000000000 个苹果")
        if achievement_35_on == 1: achievement_35_get = 1; achievement_get("无底洞", "收获 1000000000000000 个苹果")

        if achievement_11_on == 1: achievement_11_get = 1; achievement_get("点击！", "购买 1 个 鼠标指针")
        if achievement_12_on == 1: achievement_12_get = 1; achievement_get("双击！", "购买 2 个 鼠标指针")
        if achievement_13_on == 1: achievement_13_get = 1; achievement_get("第二双手", "购买 10 个 鼠标指针")
        if achievement_14_on == 1: achievement_14_get = 1; achievement_get("鼠标滚轮", "购买 50 个 鼠标指针")
        if achievement_15_on == 1: achievement_15_get = 1; achievement_get("无尽鼠标", "购买 100 个 鼠标指针")

        if achievement_16_on == 1: achievement_16_get = 1; achievement_get("纸制果篮", "购买 1 个 果篮")
        if achievement_17_on == 1: achievement_17_get = 1; achievement_get("竹制果篮", "购买 5 个 果篮")
        if achievement_18_on == 1: achievement_18_get = 1; achievement_get("铁制果篮", "购买 10 个 果篮")
        if achievement_19_on == 1: achievement_19_get = 1; achievement_get("钻石果篮", "购买 50 个 果篮")
        if achievement_20_on == 1: achievement_20_get = 1; achievement_get("无尽果篮", "购买 100 个 果篮")

        if achievement_21_on == 1: achievement_21_get = 1; achievement_get("老爷爷的梦想", "购买 1 个 老爷爷")
        if achievement_22_on == 1: achievement_22_get = 1; achievement_get("从没让我失望", "购买 5 个 老爷爷")
        if achievement_23_on == 1: achievement_23_get = 1; achievement_get("长者大师", "购买 10 个 老爷爷")
        if achievement_24_on == 1: achievement_24_get = 1; achievement_get("老而弥坚", "购买 50 个 老爷爷")
        if achievement_25_on == 1: achievement_25_get = 1; achievement_get("但当你变老", "购买 100 个 老爷爷")

        if achievement_26_on == 1: achievement_26_get = 1; achievement_get("就这样，埋下一颗种子", "购买 1 个 苹果树")
        if achievement_27_on == 1: achievement_27_get = 1; achievement_get("生根发芽", "购买 5 个 苹果树")
        if achievement_28_on == 1: achievement_28_get = 1; achievement_get("风吹雨打", "购买 10 个 苹果树")
        if achievement_29_on == 1: achievement_29_get = 1; achievement_get("却依然坚挺不拔", "购买 50 个 苹果树")
        if achievement_30_on == 1: achievement_30_get = 1; achievement_get("参天大树", "购买 100 个 苹果树") 
        
        if achievement_36_on == 1: achievement_36_get = 1; achievement_get("你家的后院", "购买 1 个 果园")
        if achievement_37_on == 1: achievement_37_get = 1; achievement_get("开垦荒地", "购买 5 个 果园")
        if achievement_38_on == 1: achievement_38_get = 1; achievement_get("春种秋收", "购买 10 个 果园")
        if achievement_39_on == 1: achievement_39_get = 1; achievement_get("丰收节", "购买 50 个 果园")
        if achievement_40_on == 1: achievement_40_get = 1; achievement_get("终极奉献", "购买 100 个 果园") 
        
        if achievement_41_on == 1: achievement_41_get = 1; achievement_get("小渔村之梦", "购买 1 个 水果镇")
        if achievement_42_on == 1: achievement_42_get = 1; achievement_get("致富的唯一道路", "购买 5 个 水果镇")
        if achievement_43_on == 1: achievement_43_get = 1; achievement_get("多汁小镇", "购买 10 个 水果镇")
        if achievement_44_on == 1: achievement_44_get = 1; achievement_get("现代化", "购买 50 个 水果镇")
        if achievement_45_on == 1: achievement_45_get = 1; achievement_get("苹果王国", "购买 100 个 水果镇")

        if achievement_46_on == 1: achievement_46_get = 1; achievement_get("工业时代", "购买 1 个 苹果工厂")
        if achievement_47_on == 1: achievement_47_get = 1; achievement_get("工业革命", "购买 5 个 苹果工厂")
        if achievement_48_on == 1: achievement_48_get = 1; achievement_get("全自动苹果机", "购买 10 个 苹果工厂")
        if achievement_49_on == 1: achievement_49_get = 1; achievement_get("全球变暖", "购买 50 个 苹果工厂")
        if achievement_50_on == 1: achievement_50_get = 1; achievement_get("瓦特的梦想", "购买 100 个 苹果工厂") 
        
        if achievement_51_on == 1: achievement_51_get = 1; achievement_get("成交！", "购买 1 个 水果银行")
        if achievement_52_on == 1: achievement_52_get = 1; achievement_get("一小笔钱", "购买 5 个 水果银行")
        if achievement_53_on == 1: achievement_53_get = 1; achievement_get("苹果经济学", "购买 10 个 水果银行")
        if achievement_54_on == 1: achievement_54_get = 1; achievement_get("既得利益", "购买 50 个 水果银行")
        if achievement_55_on == 1: achievement_55_get = 1; achievement_get("如此富有", "购买 100 个 水果银行")    
 
        if achievement_56_on == 1: achievement_56_get = 1; achievement_get("召唤！", "购买 1 个 魔法巫师塔")
        if achievement_57_on == 1: achievement_57_get = 1; achievement_get("魔法师的学徒", "购买 5 个 魔法巫师塔")
        if achievement_58_on == 1: achievement_58_get = 1; achievement_get("附魔的魅力", "购买 10 个 魔法巫师塔")
        if achievement_59_on == 1: achievement_59_get = 1; achievement_get("帽子太多了，兔子也不少", "购买 50 个 魔法巫师塔")
        if achievement_60_on == 1: achievement_60_get = 1; achievement_get("苹果的命运", "购买 100 个 魔法巫师塔") 
        
        if achievement_61_on == 1: achievement_61_get = 1; achievement_get("火星上有生命吗？", "购买 1 个 宇宙飞船")
        if achievement_62_on == 1: achievement_62_get = 1; achievement_get("星际高速公路", "购买 5 个 宇宙飞船")
        if achievement_63_on == 1: achievement_63_get = 1; achievement_get("遥远无际", "购买 10 个 宇宙飞船")
        if achievement_64_on == 1: achievement_64_get = 1; achievement_get("最珍贵的货物", "购买 50 个 宇宙飞船")
        if achievement_65_on == 1: achievement_65_get = 1; achievement_get("难以置信的旅途", "购买 100 个 宇宙飞船")

        if achievement_66_on == 1: achievement_66_get = 1; achievement_get("远程折跃", "购买 1 个 虫洞")
        if achievement_67_on == 1: achievement_67_get = 1; achievement_get("被虫子蛀了的苹果", "购买 5 个 虫洞")
        if achievement_68_on == 1: achievement_68_get = 1; achievement_get("一个全新的世界", "购买 10 个 虫洞")
        if achievement_69_on == 1: achievement_69_get = 1; achievement_get("空间移位", "购买 50 个 虫洞")
        if achievement_70_on == 1: achievement_70_get = 1; achievement_get("漩涡中会发生什么", "购买 100 个 虫洞") 
        
        if achievement_71_on == 1: achievement_71_get = 1; achievement_get("时空扭曲", "购买 1 个 时光机")
        if achievement_72_on == 1: achievement_72_get = 1; achievement_get("可折叠时间线", "购买 5 个 时光机")
        if achievement_73_on == 1: achievement_73_get = 1; achievement_get("重写历史", "购买 10 个 时光机")
        if achievement_74_on == 1: achievement_74_get = 1; achievement_get("消失于时间的洪流", "购买 50 个 时光机")
        if achievement_75_on == 1: achievement_75_get = 1; achievement_get("从未，永远", "购买 100 个 时光机")    

        if achievement_76_on == 1: achievement_76_get = 1; achievement_get("孤独光子", "购买 1 个 三棱镜")
        if achievement_77_on == 1: achievement_77_get = 1; achievement_get("只剩红色", "购买 5 个 三棱镜")
        if achievement_78_on == 1: achievement_78_get = 1; achievement_get("视觉幻象", "购买 10 个 三棱镜")
        if achievement_79_on == 1: achievement_79_get = 1; achievement_get("我赞美太阳", "购买 50 个 三棱镜")
        if achievement_80_on == 1: achievement_80_get = 1; achievement_get("无尽光辉", "购买 100 个 三棱镜") 
        
        if achievement_81_on == 1: achievement_81_get = 1; achievement_get("Enter", "购买 1 个 Python 控制台")
        if achievement_82_on == 1: achievement_82_get = 1; achievement_get("命名空间的胜利", "购买 5 个 Python 控制台")
        if achievement_83_on == 1: achievement_83_get = 1; achievement_get("简洁，复杂与凌乱", "购买 10 个 Python 控制台")
        if achievement_84_on == 1: achievement_84_get = 1; achievement_get("扁平胜于嵌套", "购买 50 个 Python 控制台")
        if achievement_85_on == 1: achievement_85_get = 1; achievement_get("人生苦短", "购买 100 个 Python 控制台")    
        
        time.sleep(1)

def newspaper_logic():  # 报纸逻辑线程
    global newspaper
    time.sleep(1)
    while True:
        newspaper['text'] = "报纸\n\n"+get_news()[random.randint(0,len(get_news())-1)]
        time.sleep(5)

########## 其他窗口 ##########

def blank(win,rows=int,columns=int):  # 占位符
    blank = tk.Label(win,text="     ")
    blank.grid(row=rows,column=columns)

def window_download():  # 存档下载窗口
    click_sound()
    rootdownload = tk.Tk()
    rootdownload.title("导出存档")
    rootdownload.resizable(0, 0)

    encode_string: str = str(apple_amount) + "|" + str(apple_amount_total) + "|" + str(sponsor_amount) + "|" + str(
        seed_amount) + "|" + str(basket_amount) + "|" + str(tree_amount) + "|" + str(garden_amount) + "|" + str(
        town_amount) + "|" + str(country_amount) + "|" + str(planet_amount) + "|" + str(wizardtower_amount) + "|" + str(
        plane_amount) + "|" + str(hole_amount) + "|" + str(timemachine_amount) + "|" + str(glass_amount) + "|" + str(
        js_amount) + "|" + str(click_time)

    str_encoded = cryptocode.encrypt(encode_string, "Minecraft is love, minecraft is life, minecraft is everything! ")

    save_download_label = tk.Label(rootdownload, text="请妥善储存以下字符串。"
                                                      "下次游戏时，点击 “导入存档” 按钮并粘帖该字符串以继续游戏！")
    save_download_label.pack()

    save_download_entry = tk.Entry(rootdownload, width=150, justify='center')
    save_download_entry.insert(0, str_encoded)
    save_download_entry.pack()

    def download_close():
        click_sound()
        rootdownload.destroy()

    save_download_button = tk.Button(rootdownload, width=10, text="关闭..",
                         cursor='hand2',
                         overrelief='sunken',command=download_close)
    save_download_button.pack()

    rootdownload.mainloop()

def window_upload():  # 存档上传窗口
    click_sound()
    rootupload = tk.Tk()
    rootupload.title("导入存档")
    rootupload.resizable(0, 0)

    save_upload_label = tk.Label(rootupload, text="请输入上次游戏保存的字符串以继续游戏！")
    save_upload_label.pack()

    save_upload_entry = tk.Entry(rootupload, width=150, justify='center')
    save_upload_entry.pack()

    def upload():
        click_sound()
        global apple_amount, apple_amount_total
        global sponsor_amount, seed_amount, basket_amount, tree_amount, garden_amount
        global town_amount, country_amount, planet_amount, wizardtower_amount, plane_amount
        global hole_amount, timemachine_amount, glass_amount, js_amount
        global click_time
        global button_clicked_amount_2, button_clicked_amount_3, button_clicked_amount_4, button_clicked_amount_5
        global button_clicked_amount_6, button_clicked_amount_7, button_clicked_amount_8, button_clicked_amount_9
        global button_clicked_amount_10, button_clicked_amount_11, button_clicked_amount_12, button_clicked_amount_13
        global button_clicked_amount_14, button_clicked_amount_15
        global price_sponsor, price_seed, price_basket, price_tree, price_garden
        global price_town, price_country, price_planet, price_wizardtower, price_plane
        global price_hole, price_timemachine, price_glass, price_js

        get_string = save_upload_entry.get()
        str_decoded = cryptocode.decrypt(get_string, "Minecraft is love, minecraft is life, minecraft is everything! ")

        tuple_ud = str_decoded.split("|")
        apple_amount = int(tuple_ud[0])
        apple_amount_total = int(tuple_ud[1])
        sponsor_amount = int(tuple_ud[2])
        seed_amount = int(tuple_ud[3])
        basket_amount = int(tuple_ud[4])
        tree_amount = int(tuple_ud[5])
        garden_amount = int(tuple_ud[6])
        town_amount = int(tuple_ud[7])
        country_amount = int(tuple_ud[8])
        planet_amount = int(tuple_ud[9])
        wizardtower_amount = int(tuple_ud[10])
        plane_amount = int(tuple_ud[11])
        hole_amount = int(tuple_ud[12])
        timemachine_amount = int(tuple_ud[13])
        glass_amount = int(tuple_ud[14])
        js_amount = int(tuple_ud[15])
        click_time = int(tuple_ud[16])

        button_clicked_amount_2 += sponsor_amount
        price_sponsor += button_clicked_amount_2
        button_clicked_amount_3 += seed_amount
        price_seed += button_clicked_amount_3
        button_clicked_amount_4 += basket_amount
        price_basket += button_clicked_amount_4
        button_clicked_amount_5 += tree_amount
        price_tree += button_clicked_amount_5
        button_clicked_amount_6 += garden_amount
        price_garden += button_clicked_amount_6
        button_clicked_amount_7 += town_amount
        price_town += button_clicked_amount_7
        button_clicked_amount_8 += country_amount
        price_country += button_clicked_amount_8
        button_clicked_amount_9 += planet_amount
        price_planet += button_clicked_amount_9
        button_clicked_amount_10 += wizardtower_amount
        price_wizardtower += button_clicked_amount_10
        button_clicked_amount_11 += plane_amount
        price_plane += button_clicked_amount_11
        button_clicked_amount_12 += hole_amount
        price_hole += button_clicked_amount_12
        button_clicked_amount_13 += timemachine_amount
        price_timemachine += button_clicked_amount_13
        button_clicked_amount_14 += glass_amount
        price_glass += button_clicked_amount_14
        button_clicked_amount_15 += js_amount
        price_js += button_clicked_amount_15

    save_upload_button = tk.Button(rootupload, width=10,
                         cursor='hand2',
                         overrelief='sunken', text="导入..", command=upload)
    save_upload_button.pack()

    rootupload.mainloop()

def window_about():  # 关于窗口
    click_sound()
    rootabout = tk.Toplevel()
    rootabout.title("关于：苹果点点乐 Apple Clicker©")
    rootabout.resizable(0, 0)

    def SaveLastClickPos(event):  # 窗口拖动
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + rootabout.winfo_x(), event.y - lastClickY + rootabout.winfo_y()
        rootabout.geometry("+%s+%s" % (x , y))

    rootabout.bind('<Button-1>', SaveLastClickPos)
    rootabout.bind('<B1-Motion>', Dragging)

    frame_icon = tk.Frame(rootabout,padx=50)
    frame_icon.grid(row=0,column=0)

    icon_img = tk.PhotoImage(file='./assets/app.gif')
    icon_label = tk.Label(frame_icon, image=icon_img)
    icon_label.pack(anchor='center', pady=40)

    icon_label_title = tk.Label(frame_icon, text=("苹果点点乐 Apple Clicker©  " + ver), font=("Arial", 17))
    icon_label_title.pack(anchor='center')

    icon_label_title = tk.Label(frame_icon, text="作者/版权: 轩哥啊哈OvO/Xuange_Aha", font=("Arial", 13))
    icon_label_title.pack(anchor='center')

    button_frame = tk.Frame(frame_icon)
    button_frame.pack(anchor='center')

    def log_clicked():
        click_sound()
        file_open = open("log/logs.txt", "r", encoding='utf-8')
        file_log = file_open.read()
        file_open.close()

        text_about.delete(1.0, tk.END)
        text_about.insert("insert", file_log)

    def credit_clicked():
        click_sound()
        file_open = open("log/credits.txt", "r", encoding='utf-8')
        file_log = file_open.read()
        file_open.close()

        text_about.delete(1.0, tk.END)
        text_about.insert("insert", file_log)

    def module_clicked():
        click_sound()
        file_open = open("log/modules.txt", "r", encoding='utf-8')
        file_log = file_open.read()
        file_open.close()

        text_about.delete(1.0, tk.END)
        text_about.insert("insert", file_log)

    button_log = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken', text="更新信息..",command=log_clicked)
    button_log.grid(row=1, column=1)

    blank(button_frame,1,2)

    button_credit = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken', text="制作者..",command=credit_clicked)
    button_credit.grid(row=1, column=3)

    blank(button_frame,1,4)

    button_module = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken',text="使用模块..",command=module_clicked)
    button_module.grid(row=1, column=5)

    frame_text = tk.Frame(rootabout,padx=15,pady=15)
    frame_text.grid(row=0,column=1)

    text_about = tk.Text(frame_text,width=60)
    text_about.pack()

    file_open = open("log/logs.txt", "r", encoding='utf-8')
    file_log = file_open.read()
    file_open.close()

    text_about.delete(1.0, tk.END)
    text_about.insert("insert", file_log)

    rootabout.mainloop()

def window_cheat():  # 作弊传送门窗口
    click_sound()
    rootcheat = tk.Tk()
    rootcheat.title("作弊传送门")
    rootcheat.resizable(0, 0)

    cheat_label = tk.Label(rootcheat, text="作弊而得的苹果尝起来很难吃，不是吗？")
    cheat_label.grid(row=1,column=1,columnspan=3)

    cheat_entry = tk.Entry(rootcheat, width=100, justify='center')
    cheat_entry.grid(row=2,column=1,columnspan=3)

    def cheat_process():
        click_sound()
        global apple_amount, apple_amount_total
        cheat = cheat_entry.get().split(" ")

        if cheat[0] == '/earn':
            if cheat[1] == 'apple':
                try:
                    cheat_add = int(cheat[2])
                    apple_amount += cheat_add
                    apple_amount_total += cheat_add
                except:
                    pass

    save_cheat_button = tk.Button(rootcheat, width=10, text="加载..",
                                cursor='hand2', overrelief='sunken',command=cheat_process)
    save_cheat_button.grid(row=3,column=1)

    def cheat_close():
        click_sound()
        rootcheat.destroy()

    close_cheat_button = tk.Button(rootcheat, width=10, text="关闭..", 
                                cursor='hand2', overrelief='sunken', command=cheat_close)
    close_cheat_button.grid(row=3,column=3)

    rootcheat.mainloop()

def window_settings():  # 设置窗口
    click_sound()
    rootsettings = tk.Tk()
    rootsettings.title("游戏设置")
    rootsettings.resizable(0, 0)

    def SaveLastClickPos(event):  # 窗口拖动
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + rootsettings.winfo_x(), event.y - lastClickY + rootsettings.winfo_y()
        root.geometry("+%s+%s" % (x , y))

    rootsettings.bind('<Button-1>', SaveLastClickPos)
    rootsettings.bind('<B1-Motion>', Dragging)

    blank(rootsettings,0,0)
    
    blank(rootsettings,0,3)

    def togglemusic():
        global music_on, information
        if music_on == 1:
            set_1_button['text'] = "开启"
            information = "设置：音效已关闭"
            music_on = 0
        else:
            set_1_button['text'] = "关闭"
            information = "设置：音效已开启"
            music_on = 1

    set_1_label = tk.Label(rootsettings,text="音效：  ")
    set_1_label.grid(row=1,column=1)

    set_1_button = tk.Button(rootsettings,command=togglemusic,width=10)
    set_1_button.grid(row=1,column=2)

    if music_on == 1:
        set_1_button['text'] = "关闭"
    else:
        set_1_button['text'] = "开启"

    blank(rootsettings,10,0)
    
    blank(rootsettings,10,3)

    rootsettings.mainloop()

def root_close():  # 窗口关闭
    root.destroy()
    sys.exit()

########## 主窗口 ##########

root = tk.Tk()
root.title("Apple Clicker© " + ver)
root.iconphoto(True, tk.PhotoImage(file='./assets/app.png'))
root.resizable(0, 0)

def SaveLastClickPos(event):  # 窗口拖动
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

style = ttk.Style(theme='journal')  # ttk窗口主题

auto_amount_add_per_second_thread = threading.Thread(target=main_operation_logic)  # 逻辑线程启动
auto_amount_add_per_second_thread.start()

upgrade_price_thread = threading.Thread(target=upgrade_price_logic)
upgrade_price_thread.start()

progress_bar_thread = threading.Thread(target=progress_bar_logic)
progress_bar_thread.start()

achievement_thread = threading.Thread(target=achievement_logic)
achievement_thread.start()

newspaper_thread = threading.Thread(target=newspaper_logic)
newspaper_thread.start()

##### 左侧框架 #####

frame_left = tk.Frame(root, padx=30)
frame_left.grid(row=1, column=1, rowspan=3)

apple_amount_entry = tk.Entry(frame_left, justify='center', font=("", "14"), width=16)  # 左侧信息栏
apple_amount_entry.pack()
apple_per_click_entry = tk.Entry(frame_left, width=23)
apple_per_click_entry.pack()
apple_per_second_entry = tk.Entry(frame_left, width=23)
apple_per_second_entry.pack()
apple_amount_entry.after(recursion_time, apple_amount_entry_update)

apple_img = tk.PhotoImage(file="./assets/app.png")

button_click = tk.Button(frame_left,width=160, height=160, image=apple_img, 
                         cursor='hand2', overrelief='sunken', command=click_button_clicked)  # 苹果点击按钮
button_click.pack()

blank_pack = tk.Label(frame_left,text="     ")
blank_pack.pack()

newspaper = tk.Button(frame_left,width=20,height=5,cursor='hand2',overrelief='sunken',command=refresh_newspaper)
newspaper.pack()

##### 中间框架 #####

frame_button = tk.Frame(root)
frame_button.grid(row=1, column=2)

button_sponsor = tk.Button(frame_button, text="购买 鼠标指针", cursor='hand2', overrelief='sunken',command=sponsor_button_clicked)  # 建筑购买按钮
button_sponsor.grid(row=2, column=1)
button_seed = tk.Button(frame_button, text="购买 果篮",cursor='hand2', overrelief='sunken',command=seed_button_clicked)
button_seed.grid(row=3, column=1)
button_basket = tk.Button(frame_button, text="购买 老爷爷", cursor='hand2', overrelief='sunken', command=basket_button_clicked)
button_basket.grid(row=4, column=1)
button_tree = tk.Button(frame_button, text="购买 苹果树", cursor='hand2', overrelief='sunken',command=tree_button_clicked)
button_tree.grid(row=5, column=1)
button_garden = tk.Button(frame_button, text="购买 果园", cursor='hand2', overrelief='sunken', command=garden_button_clicked)
button_garden.grid(row=6, column=1)
button_town = tk.Button(frame_button, text="购买 水果镇", cursor='hand2', overrelief='sunken', command=town_button_clicked)
button_town.grid(row=7, column=1)
button_country = tk.Button(frame_button, text="购买 苹果工厂", cursor='hand2', overrelief='sunken',command=country_button_clicked)
button_country.grid(row=8, column=1)
button_planet = tk.Button(frame_button, text="购买 水果银行", cursor='hand2', overrelief='sunken', command=planet_button_clicked)
button_planet.grid(row=9, column=1)
button_wizardtower = tk.Button(frame_button, text="购买 魔法巫师塔", cursor='hand2', overrelief='sunken', command=wizardtower_button_clicked)
button_wizardtower.grid(row=10, column=1)
button_plane = tk.Button(frame_button, text="购买 宇宙飞船", cursor='hand2', overrelief='sunken', command=plane_button_clicked)
button_plane.grid(row=11, column=1)
button_hole = tk.Button(frame_button, text="购买 虫洞", cursor='hand2', overrelief='sunken', command=hole_button_clicked)
button_hole.grid(row=12, column=1)
button_timemachine = tk.Button(frame_button, text="购买 时光机", cursor='hand2', overrelief='sunken', command=timemachine_button_clicked)
button_timemachine.grid(row=13, column=1)
button_glass = tk.Button(frame_button, text="购买 三棱镜", cursor='hand2', overrelief='sunken', command=glass_button_clicked)
button_glass.grid(row=14, column=1)
button_js = tk.Button(frame_button, text="购买 Python 控制台", cursor='hand2', overrelief='sunken', command=js_button_clicked)
button_js.grid(row=15, column=1)

label_2 = tk.Label(frame_button, text="让这些可爱的鼠标们帮你一起点点点！")  # 建筑简介
label_2.grid(row=2, column=2)
label_3 = tk.Label(frame_button, text="多精致而美丽的果篮啊，记得周末家庭野餐时带上它！")
label_3.grid(row=3, column=2)
label_4 = tk.Label(frame_button, text="慈祥和蔼的老爷爷，来到你身边完成他们的梦想！")
label_4.grid(row=4, column=2)
label_5 = tk.Label(frame_button, text="这种特殊品种的苹果树一年四季都可以结果！")
label_5.grid(row=5, column=2)
label_6 = tk.Label(frame_button, text="从现在开始，在你家后院种下苹果！")
label_6.grid(row=6, column=2)
label_7 = tk.Label(frame_button, text="水果镇里，种苹果、吃苹果是家家户户的最爱！")
label_7.grid(row=7, column=2)
label_8 = tk.Label(frame_button, text="是时候开启工业革命，让苹果农业自动化！")
label_8.grid(row=8, column=2)
label_9 = tk.Label(frame_button, text="在水果镇的银行投资，但货币是苹果！")
label_9.grid(row=9, column=2)
label_10 = tk.Label(frame_button, text="通过魔法巫师塔召唤大量的苹果！")
label_10.grid(row=10, column=2)
label_11 = tk.Label(frame_button, text="几百年了，人们终于在宇宙的深处发现了有机物的存在！")
label_11.grid(row=11, column=2)
label_12 = tk.Label(frame_button, text="再远一点，前往平行宇宙寻找苹果！")
label_12.grid(row=12, column=2)
label_13 = tk.Label(frame_button, text="回到过去，前往将来，占领时空中的所有苹果！")
label_13.grid(row=13, column=2)
label_14 = tk.Label(frame_button, text="把宇宙中的反物质等价交换凝聚为苹果！")
label_14.grid(row=14, column=2)
label_15 = tk.Label(frame_button, text="     "+"人生苦短，最终你用 Python 让你的苹果之路走向无尽！"+"     ")
label_15.grid(row=15, column=2)

information_label_column_1 = tk.Label(frame_button, text="建筑")  # 栏目标题
information_label_column_1.grid(row=1, column=1, pady=2)
information_label_column_2 = tk.Label(frame_button, text="建筑简介")
information_label_column_2.grid(row=1, column=2, pady=2)
information_label_column_3 = tk.Label(frame_button, text="数量")
information_label_column_3.grid(row=1, column=3, pady=2)
information_label_column_4 = tk.Label(frame_button, text="价格")
information_label_column_4.grid(row=1, column=4, pady=2)
information_label_column_5 = tk.Label(frame_button, text="速度")
information_label_column_5.grid(row=1, column=5, pady=2)
information_label_column_6 = tk.Label(frame_button, text="成就栏")
information_label_column_6.grid(row=1, column=6, pady=2,columnspan=2)

entry_information_number_23 = tk.Entry(frame_button, width=5)  # 信息网格
entry_information_number_23.grid(row=2, column=3)
entry_information_number_33 = tk.Entry(frame_button, width=5)
entry_information_number_33.grid(row=3, column=3)
entry_information_number_43 = tk.Entry(frame_button, width=5)
entry_information_number_43.grid(row=4, column=3)
entry_information_number_53 = tk.Entry(frame_button, width=5)
entry_information_number_53.grid(row=5, column=3)
entry_information_number_63 = tk.Entry(frame_button, width=5)
entry_information_number_63.grid(row=6, column=3)
entry_information_number_73 = tk.Entry(frame_button, width=5)
entry_information_number_73.grid(row=7, column=3)
entry_information_number_83 = tk.Entry(frame_button, width=5)
entry_information_number_83.grid(row=8, column=3)
entry_information_number_93 = tk.Entry(frame_button, width=5)
entry_information_number_93.grid(row=9, column=3)
entry_information_number_103 = tk.Entry(frame_button, width=5)
entry_information_number_103.grid(row=10, column=3)
entry_information_number_113 = tk.Entry(frame_button, width=5)
entry_information_number_113.grid(row=11, column=3)
entry_information_number_123 = tk.Entry(frame_button, width=5)
entry_information_number_123.grid(row=12, column=3)
entry_information_number_133 = tk.Entry(frame_button, width=5)
entry_information_number_133.grid(row=13, column=3)
entry_information_number_143 = tk.Entry(frame_button, width=5)
entry_information_number_143.grid(row=14, column=3)
entry_information_number_153 = tk.Entry(frame_button, width=5)
entry_information_number_153.grid(row=15, column=3)

entry_information_number_24 = tk.Entry(frame_button, width=11)
entry_information_number_24.grid(row=2, column=4)
entry_information_number_34 = tk.Entry(frame_button, width=11)
entry_information_number_34.grid(row=3, column=4)
entry_information_number_44 = tk.Entry(frame_button, width=11)
entry_information_number_44.grid(row=4, column=4)
entry_information_number_54 = tk.Entry(frame_button, width=11)
entry_information_number_54.grid(row=5, column=4)
entry_information_number_64 = tk.Entry(frame_button, width=11)
entry_information_number_64.grid(row=6, column=4)
entry_information_number_74 = tk.Entry(frame_button, width=11)
entry_information_number_74.grid(row=7, column=4)
entry_information_number_84 = tk.Entry(frame_button, width=11)
entry_information_number_84.grid(row=8, column=4)
entry_information_number_94 = tk.Entry(frame_button, width=11)
entry_information_number_94.grid(row=9, column=4)
entry_information_number_104 = tk.Entry(frame_button, width=11)
entry_information_number_104.grid(row=10, column=4)
entry_information_number_114 = tk.Entry(frame_button, width=11)
entry_information_number_114.grid(row=11, column=4)
entry_information_number_124 = tk.Entry(frame_button, width=11)
entry_information_number_124.grid(row=12, column=4)
entry_information_number_134 = tk.Entry(frame_button, width=11)
entry_information_number_134.grid(row=13, column=4)
entry_information_number_144 = tk.Entry(frame_button, width=11)
entry_information_number_144.grid(row=14, column=4)
entry_information_number_154 = tk.Entry(frame_button, width=11)
entry_information_number_154.grid(row=15, column=4)

entry_information_number_30 = tk.Entry(frame_button, width=12)
entry_information_number_30.grid(row=2, column=5)
entry_information_number_35 = tk.Entry(frame_button, width=12)
entry_information_number_35.grid(row=3, column=5)
entry_information_number_45 = tk.Entry(frame_button, width=12)
entry_information_number_45.grid(row=4, column=5)
entry_information_number_55 = tk.Entry(frame_button, width=12)
entry_information_number_55.grid(row=5, column=5)
entry_information_number_65 = tk.Entry(frame_button, width=12)
entry_information_number_65.grid(row=6, column=5)
entry_information_number_75 = tk.Entry(frame_button, width=12)
entry_information_number_75.grid(row=7, column=5)
entry_information_number_85 = tk.Entry(frame_button, width=12)
entry_information_number_85.grid(row=8, column=5)
entry_information_number_95 = tk.Entry(frame_button, width=12)
entry_information_number_95.grid(row=9, column=5)
entry_information_number_105 = tk.Entry(frame_button, width=12)
entry_information_number_105.grid(row=10, column=5)
entry_information_number_115 = tk.Entry(frame_button, width=12)
entry_information_number_115.grid(row=11, column=5)
entry_information_number_130 = tk.Entry(frame_button, width=12)
entry_information_number_130.grid(row=12, column=5)
entry_information_number_135 = tk.Entry(frame_button, width=12)
entry_information_number_135.grid(row=13, column=5)
entry_information_number_145 = tk.Entry(frame_button, width=12)
entry_information_number_145.grid(row=14, column=5)
entry_information_number_155 = tk.Entry(frame_button, width=12)
entry_information_number_155.grid(row=15, column=5)
entry_information_number_155.after(recursion_time, entry_information_number_upgrade)

achievements_information_text = tk.Text(frame_button, width=45, height=31)  # 成就框
achievements_information_text.grid(row=2, column=6, rowspan=13,columnspan=2)

achevement_num_all = 85

achievement_progress_bar = tk.ttk.Progressbar(frame_button, length=300, maximum=achevement_num_all, orient='horizontal', mode='determinate')
achievement_progress_bar.grid(row=15, column=6)
achievement_progress_entry = tk.Entry(frame_button,width=5)
achievement_progress_entry.grid(row=15, column=7)
achievement_progress_entry.after(recursion_time, achievement_progress_update)

##### 下侧框架 #####

frame_information = tk.Frame(root)
frame_information.grid(row=2, column=2)

statistics_text_label = tk.Label(frame_information, text="统计信息")  # 统计信息框
statistics_text_label.grid(row=1, column=1, pady=2)
statistics_text_label = tk.Label(frame_information, text="升级")
statistics_text_label.grid(row=1, column=3, columnspan=2, pady=2, padx=100)
statistics_text = tk.Text(frame_information, height=8, width=40, font=("", 11))
statistics_text.grid(row=2, column=1, rowspan=10)
statistics_text.after(recursion_time, statistics_text_upgrade)

upgrade_button_2 = tk.Button(frame_information, text="升级..", width=10, height=2,
                            cursor='hand2', overrelief='sunken', command=upgrade_button_clicked)
upgrade_button_2.grid(row=2, column=3, rowspan=2, sticky='e')
upgrade_button_entry = tk.Entry(frame_information)
upgrade_button_entry.grid(row=2, column=4)
upgrade_button_entry_price = tk.Entry(frame_information)
upgrade_button_entry_price.grid(row=3, column=4, sticky='n')
upgrade_button_entry.after(recursion_time, upgrade_button_entry_update)

time_entry = tk.Entry(frame_information,justify='center',width=30,borderwidth=0)
time_entry.grid(row=4,column=3,columnspan=2,padx=10)
time_entry.after(300,time_entry_update)

##### 底部框架 #####

frame_bottom = tk.Frame(root)
frame_bottom.grid(row=3, column=1, columnspan=2)

level_progress_label_left = tk.Entry(frame_bottom, width=7, borderwidth=1, justify='center')  # 等级进度条
level_progress_label_left.grid(row=1, column=0)
level_progress_label_right = tk.Entry(frame_bottom, width=7, borderwidth=1, justify='center')
level_progress_label_right.grid(row=1, column=2)
level_progress_bar = tk.ttk.Progressbar(frame_bottom, length=300, orient='horizontal', mode='determinate')
level_progress_bar.grid(row=1, column=1)
level_progress_bar.after(recursion_time, level_progress_bar_update)

entry_information_information = tk.Entry(frame_bottom, width=80, justify='center')
entry_information_information.grid(row=1, column=4, ipady=1, pady=5, padx=50)
entry_information_information.after(recursion_time, entry_information_information_upgrade)

##### 底部按钮框架 #####

frame_buttons = tk.Frame(frame_bottom)
frame_buttons.grid(row=1, column=11,columnspan=2)

bottom_button_download = tk.Button(frame_buttons, text="导出存档..", width=10, height=1, pady=3,
                                   cursor='hand2', overrelief='sunken', command=window_download)
bottom_button_download.grid(row=1, column=2, sticky='w')


bottom_button_upload = tk.Button(frame_buttons, text="导入存档..", width=10, height=1, pady=3,
                                 cursor='hand2', overrelief='sunken', command=window_upload)
bottom_button_upload.grid(row=1, column=4, sticky='w')


bottom_button_about = tk.Button(frame_buttons, text="退出..", width=8, height=1, pady=3,
                                cursor='hand2', overrelief='sunken', command=root_close)
bottom_button_about.grid(row=1, column=6, sticky='w')

##### 工具栏 #####

menubar = tk.Menu(root, bg="red")
root.config(menu=menubar)

operationMenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="关于..", menu=operationMenu)
operationMenu.add_command(label="关于", command=window_about)

operationMenu.add_command(label="设置", command=window_settings)
operationMenu.add_command(label="传送门", command=window_cheat)

exitMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="退出..", menu=exitMenu)
exitMenu.add_command(label="退出", command=root_close)

root.mainloop()

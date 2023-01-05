import sys  # 导入模块
import time
import random
import pygame
import threading
import cryptocode
import tkinter as tk
from ttkbootstrap import Style
from win10toast import ToastNotifier

ver: str = 'beta0.4.0'  # 版本号

apple_amount: int = 0  # 初始化定义
apple_amount_total: int = 0

sponsor_amount: int = 0
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

building_amount: int = 0

price_sponsor: int = 10
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

value_sponsor: float = 0.5
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

button_clicked_amount_2: int = 0
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

click_time: int = 0

upgrade_price: int = 200000
upgrade_button_clicked_time: int = 0

level_progress_now: int = 1
left_label = "Level " + str(level_progress_now)
right_label = "Level " + str(level_progress_now + 1)

difficulty_add_multiply: float = 1.2

achievement_1_on: int = 0
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
achievement_1_get: int = 0
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

information: str = "欢迎来到 苹果点点乐©!  作者/版权: 轩哥啊哈OvO/Xuange_Aha"  # 初始信息

def main_main_operation_logic():  # 主要运算逻辑线程
    global apple_amount
    global apple_amount_total
    global building_amount
    whee = 0
    while whee == 0:
        global auto_add_per_second
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
                                   (js_amount * value_js)) * pow(1.02, upgrade_button_clicked_time + 1))
        apple_amount += auto_add_per_second
        apple_amount_total += auto_add_per_second
        global add_per_click
        add_per_click = int((sponsor_amount * 1) + \
                            (seed_amount * 1.30) + \
                            (basket_amount * 1.5) + \
                            (tree_amount * 1.75) + \
                            (garden_amount * 2) + \
                            (town_amount * 2.30) + \
                            (country_amount * 2.5) + \
                            (planet_amount * 2.75) + \
                            (wizardtower_amount * 3) + \
                            (plane_amount * 3.30) + \
                            (hole_amount * 3.5) + \
                            (timemachine_amount * 3.75) + \
                            (glass_amount * 4) + \
                            (js_amount * 5) + 1)
        building_amount = sponsor_amount + seed_amount + basket_amount + tree_amount + garden_amount + \
                          town_amount + country_amount + planet_amount + wizardtower_amount + \
                          plane_amount + hole_amount + timemachine_amount + glass_amount + js_amount
        time.sleep(1)

def upgrade_price_logic():
    global upgrade_price
    whaa = 0
    while whaa == 0:
        upgrade_price = int(200000 * pow(1.2, upgrade_button_clicked_time))
        time.sleep(1)

def progress_bar_logic():
    global level_progress_now
    whoo = 0
    while whoo == 0:
        if apple_amount_total < 12000:
            level_progress_now = 1
        elif 12000 < apple_amount_total < 60000:
            level_progress_now = 2
        elif 60000 < apple_amount_total < 200000:
            level_progress_now = 3
        elif 200000 < apple_amount_total < 1000000:
            level_progress_now = 4
        elif 1000000 < apple_amount_total < 5500000:
            level_progress_now = 5
        elif 5500000 < apple_amount_total < 18000000:
            level_progress_now = 6
        elif 18000000 < apple_amount_total < 60000000:
            level_progress_now = 7
        elif 60000000 < apple_amount_total < 200000000:
            level_progress_now = 8
        elif 200000000 < apple_amount_total < 1000000000:
            level_progress_now = 9
        else:
            level_progress_now = 10
        time.sleep(0.5)

def achievement_logic():
    global information
    global achievement_1_get
    global achievement_2_get
    global achievement_3_get
    global achievement_4_get
    global achievement_5_get
    global achievement_6_get
    global achievement_7_get
    global achievement_8_get
    global achievement_9_get
    global achievement_10_get
    global achievement_11_get
    global achievement_12_get
    global achievement_13_get
    global achievement_14_get
    global achievement_15_get
    global achievement_16_get
    global achievement_17_get
    global achievement_18_get
    global achievement_19_get
    global achievement_20_get
    global achievement_21_get
    global achievement_22_get
    global achievement_23_get
    global achievement_24_get
    global achievement_25_get
    global achievement_26_get
    global achievement_27_get
    global achievement_28_get
    global achievement_29_get
    global achievement_30_get
    global achievement_31_get
    global achievement_32_get
    global achievement_33_get
    global achievement_34_get
    global achievement_35_get
    global achievement_36_get
    global achievement_37_get
    global achievement_38_get
    global achievement_39_get
    global achievement_40_get
    global achievement_41_get
    global achievement_42_get
    global achievement_45_get
    global achievement_44_get
    global achievement_45_get
    
    achievement = ToastNotifier()

    def achievement_get_sound():
        pygame.mixer.init()
        pygame.mixer.music.load(r"./sound/Random_levelup.wav")
        pygame.mixer.music.play(start=0.0)

    def achievement_get(title,rule):
        global information
        information = "恭喜你 获得成就 ["+title+"]："+rule+"！"
        achievement_get_sound()
        toast_title = "获得成就 ["+title+"]"
        achievements_information_text.insert(tk.END, toast_title + ": " + rule + "\n")
        achievement.show_toast(title=toast_title, msg=rule,
                               icon_path="./assets/app16x16.ico", duration=5)

    whao = 0
    while whao == 0:
        if apple_amount >= 1 and achievement_1_get == 0:
            achievement_1_on = 1
        else:
            achievement_1_on = 0
        if apple_amount >= 100 and achievement_2_get == 0:
            achievement_2_on = 1
        else:
            achievement_2_on = 0
        if apple_amount >= 1000 and achievement_3_get == 0:
            achievement_3_on = 1
        else:
            achievement_3_on = 0
        if apple_amount >= 10000 and achievement_4_get == 0:
            achievement_4_on = 1
        else:
            achievement_4_on = 0
        if apple_amount >= 100000 and achievement_5_get == 0:
            achievement_5_on = 1
        else:
            achievement_5_on = 0
        if apple_amount >= 1000000 and achievement_6_get == 0:
            achievement_6_on = 1
        else:
            achievement_6_on = 0
        if apple_amount >= 10000000 and achievement_7_get == 0:
            achievement_7_on = 1
        else:
            achievement_7_on = 0
        if apple_amount >= 100000000 and achievement_8_get == 0:
            achievement_8_on = 1
        else:
            achievement_8_on = 0
        if apple_amount >= 1000000000 and achievement_9_get == 0:
            achievement_9_on = 1
        else:
            achievement_9_on = 0
        if apple_amount >= 10000000000 and achievement_10_get == 0:
            achievement_10_on = 1
        else:
            achievement_10_on = 0
        if apple_amount >= 100000000000 and achievement_31_get == 0:
            achievement_31_on = 1
        else:
            achievement_31_on = 0
        if apple_amount >= 1000000000000 and achievement_32_get == 0:
            achievement_32_on = 1
        else:
            achievement_32_on = 0
        if apple_amount >= 10000000000000 and achievement_33_get == 0:
            achievement_33_on = 1
        else:
            achievement_33_on = 0
        if apple_amount >= 100000000000000 and achievement_34_get == 0:
            achievement_34_on = 1
        else:
            achievement_34_on = 0
        if apple_amount >= 1000000000000000 and achievement_35_get == 0:
            achievement_35_on = 1
        else:
            achievement_35_on = 0

        if sponsor_amount >= 1 and achievement_11_get == 0:
            achievement_11_on = 1
        else:
            achievement_11_on = 0
        if sponsor_amount >= 2 and achievement_12_get == 0:
            achievement_12_on = 1
        else:
            achievement_12_on = 0
        if sponsor_amount >= 10 and achievement_13_get == 0:
            achievement_13_on = 1
        else:
            achievement_13_on = 0
        if sponsor_amount >= 50 and achievement_14_get == 0:
            achievement_14_on = 1
        else:
            achievement_14_on = 0
        if sponsor_amount >= 100 and achievement_15_get == 0:
            achievement_15_on = 1
        else:
            achievement_15_on = 0

        if seed_amount >= 1 and achievement_16_get == 0:
            achievement_16_on = 1
        else:
            achievement_16_on = 0
        if seed_amount >= 5 and achievement_17_get == 0:
            achievement_17_on = 1
        else:
            achievement_17_on = 0
        if seed_amount >= 10 and achievement_18_get == 0:
            achievement_18_on = 1
        else:
            achievement_18_on = 0
        if seed_amount >= 50 and achievement_19_get == 0:
            achievement_19_on = 1
        else:
            achievement_19_on = 0
        if seed_amount >= 100 and achievement_20_get == 0:
            achievement_20_on = 1
        else:
            achievement_20_on = 0

        if basket_amount >= 1 and achievement_21_get == 0:
            achievement_21_on = 1
        else:
            achievement_21_on = 0
        if basket_amount >= 5 and achievement_22_get == 0:
            achievement_22_on = 1
        else:
            achievement_22_on = 0
        if basket_amount >= 10 and achievement_23_get == 0:
            achievement_23_on = 1
        else:
            achievement_23_on = 0
        if basket_amount >= 50 and achievement_24_get == 0:
            achievement_24_on = 1
        else:
            achievement_24_on = 0
        if basket_amount >= 100 and achievement_25_get == 0:
            achievement_25_on = 1
        else:
            achievement_25_on = 0
            
        if tree_amount >= 1 and achievement_26_get == 0:
            achievement_26_on = 1
        else:
            achievement_26_on = 0
        if tree_amount >= 5 and achievement_27_get == 0:
            achievement_27_on = 1
        else:
            achievement_27_on = 0
        if tree_amount >= 10 and achievement_28_get == 0:
            achievement_28_on = 1
        else:
            achievement_28_on = 0
        if tree_amount >= 50 and achievement_29_get == 0:
            achievement_29_on = 1
        else:
            achievement_29_on = 0
        if tree_amount >= 100 and achievement_30_get == 0:
            achievement_30_on = 1
        else:
            achievement_30_on = 0
            
        if garden_amount >= 1 and achievement_36_get == 0:
            achievement_36_on = 1
        else:
            achievement_36_on = 0
        if garden_amount >= 5 and achievement_37_get == 0:
            achievement_37_on = 1
        else:
            achievement_37_on = 0
        if garden_amount >= 10 and achievement_38_get == 0:
            achievement_38_on = 1
        else:
            achievement_38_on = 0
        if garden_amount >= 50 and achievement_39_get == 0:
            achievement_39_on = 1
        else:
            achievement_39_on = 0
        if garden_amount >= 100 and achievement_40_get == 0:
            achievement_40_on = 1
        else:
            achievement_40_on = 0
        
        if town_amount >= 1 and achievement_41_get == 0:
            achievement_41_on = 1
        else:
            achievement_41_on = 0
        if town_amount >= 5 and achievement_42_get == 0:
            achievement_42_on = 1
        else:
            achievement_42_on = 0
        if town_amount >= 10 and achievement_43_get == 0:
            achievement_43_on = 1
        else:
            achievement_43_on = 0
        if town_amount >= 50 and achievement_44_get == 0:
            achievement_44_on = 1
        else:
            achievement_44_on = 0
        if town_amount >= 100 and achievement_45_get == 0:
            achievement_45_on = 1
        else:
            achievement_45_on = 0
            
        if achievement_1_on == 1:
            achievement_1_get = 1
            achievement_get("春天的苏醒","收获 1 个苹果")
        if achievement_2_on == 1:
            achievement_2_get = 1
            achievement_get("苹果的气息", "收获 100 个苹果")
        if achievement_3_on == 1:
            achievement_3_get = 1
            achievement_get("富足果园", "收获 1000 个苹果")
        if achievement_4_on == 1:
            achievement_4_get = 1
            achievement_get("知名果园", "收获 10000 个苹果")
        if achievement_5_on == 1:
            achievement_5_get = 1
            achievement_get("现在别阻止我", "收获 100000 个苹果")
        if achievement_6_on == 1:
            achievement_6_get = 1
            achievement_get("我需要大一点的果园", "收获 1000000 个苹果")
        if achievement_7_on == 1:
            achievement_7_get = 1
            achievement_get("我这么做是为了什么？", "收获 10000000 个苹果")
        if achievement_8_on == 1:
            achievement_8_get = 1
            achievement_get("你要全吃了吗？", "收获 100000000 个苹果")
        if achievement_9_on == 1:
            achievement_9_get = 1
            achievement_get("得苹果者，得宇宙", "收获 1000000000 个苹果")
        if achievement_10_on == 1:
            achievement_10_get = 1
            achievement_get("我做过最棒的梦", "收获 10000000000 个苹果")
        if achievement_31_on == 1:
            achievement_31_get = 1
            achievement_get("我只是随便点一点", "收获 100000000000 个苹果")
        if achievement_32_on == 1:
            achievement_32_get = 1
            achievement_get("你还很饿", "收获 1000000000000 个苹果")
        if achievement_33_on == 1:
            achievement_33_get = 1
            achievement_get("最大容量", "收获 10000000000000 个苹果")
        if achievement_34_on == 1:
            achievement_34_get = 1
            achievement_get("假装，直到你摘下一颗苹果", "收获 100000000000000 个苹果")
        if achievement_35_on == 1:
            achievement_35_get = 1
            achievement_get("无底洞", "收获 1000000000000000 个苹果")

        if achievement_11_on == 1:
            achievement_11_get = 1
            achievement_get("点击！", "购买 1 个 鼠标指针")
        if achievement_12_on == 1:
            achievement_12_get = 1
            achievement_get("双击！", "购买 2 个 鼠标指针")
        if achievement_13_on == 1:
            achievement_13_get = 1
            achievement_get("第二双手", "购买 10 个 鼠标指针")
        if achievement_14_on == 1:
            achievement_14_get = 1
            achievement_get("鼠标滚轮", "购买 50 个 鼠标指针")
        if achievement_15_on == 1:
            achievement_15_get = 1
            achievement_get("无尽鼠标", "购买 100 个 鼠标指针")

        if achievement_16_on == 1:
            achievement_16_get = 1
            achievement_get("纸制果篮", "购买 1 个 果篮")
        if achievement_17_on == 1:
            achievement_17_get = 1
            achievement_get("竹制果篮", "购买 5 个 果篮")
        if achievement_18_on == 1:
            achievement_18_get = 1
            achievement_get("铁制果篮", "购买 10 个 果篮")
        if achievement_19_on == 1:
            achievement_19_get = 1
            achievement_get("钻石果篮", "购买 50 个 果篮")
        if achievement_20_on == 1:
            achievement_20_get = 1
            achievement_get("无尽果篮", "购买 100 个 果篮")

        if achievement_21_on == 1:
            achievement_21_get = 1
            achievement_get("老爷爷的梦想", "购买 1 个 老爷爷")
        if achievement_22_on == 1:
            achievement_22_get = 1
            achievement_get("从没让我失望", "购买 5 个 老爷爷")
        if achievement_23_on == 1:
            achievement_23_get = 1
            achievement_get("长者大师", "购买 10 个 老爷爷")
        if achievement_24_on == 1:
            achievement_24_get = 1
            achievement_get("老而弥坚", "购买 50 个 老爷爷")
        if achievement_25_on == 1:
            achievement_25_get = 1
            achievement_get("但当你变老", "购买 100 个 老爷爷")

        if achievement_26_on == 1:
            achievement_26_get = 1
            achievement_get("就这样，埋下一颗种子", "购买 1 个 苹果树")
        if achievement_27_on == 1:
            achievement_27_get = 1
            achievement_get("生根发芽", "购买 5 个 苹果树")
        if achievement_28_on == 1:
            achievement_28_get = 1
            achievement_get("风吹雨打", "购买 10 个 苹果树")
        if achievement_29_on == 1:
            achievement_29_get = 1
            achievement_get("却依然坚挺不拔", "购买 50 个 苹果树")
        if achievement_30_on == 1:
            achievement_30_get = 1
            achievement_get("参天大树", "购买 100 个 苹果树")
            
        if achievement_36_on == 1:
            achievement_36_get = 1
            achievement_get("微型果园", "购买 1 个 果园")
        if achievement_37_on == 1:
            achievement_37_get = 1
            achievement_get("小型果园", "购买 5 个 果园")
        if achievement_38_on == 1:
            achievement_38_get = 1
            achievement_get("中型果园", "购买 10 个 果园")
        if achievement_39_on == 1:
            achievement_39_get = 1
            achievement_get("大型果园", "购买 50 个 果园")
        if achievement_40_on == 1:
            achievement_40_get = 1
            achievement_get("巨型果园", "购买 100 个 果园")
            
        if achievement_41_on == 1:
            achievement_41_get = 1
            achievement_get("五线城镇", "购买 1 个 水果镇")
        if achievement_42_on == 1:
            achievement_42_get = 1
            achievement_get("四线城镇", "购买 5 个 水果镇")
        if achievement_43_on == 1:
            achievement_43_get = 1
            achievement_get("三线城镇", "购买 10 个 水果镇")
        if achievement_44_on == 1:
            achievement_44_get = 1
            achievement_get("二线城镇", "购买 50 个 水果镇")
        if achievement_45_on == 1:
            achievement_45_get = 1
            achievement_get("一线城镇", "购买 100 个 水果镇")
            
        time.sleep(1)

def click_button_clicked():  # 苹果按钮点击运算
    global apple_amount
    global apple_amount_total
    global click_time
    global sound_filepath
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
    apple_amount += add_per_click
    apple_amount_total += add_per_click
    click_time += 1

def successful_bought_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"./sound/Succesfull_Hit.wav")
    pygame.mixer.music.play(start=0.0)

def unsuccessful_bought_sound():
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

def sponsor_button_clicked():  # 建筑购买运算
    global apple_amount
    global price_sponsor
    global sponsor_amount
    global information
    global button_clicked_amount_2
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
    global apple_amount
    global price_seed
    global seed_amount
    global information
    global button_clicked_amount_3
    if (apple_amount - price_seed) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_seed) + " 个苹果 以购买 果篮。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 果篮。"
        successful_bought_sound()
        apple_amount -= price_seed
        button_clicked_amount_3 += 1
        price_seed += button_clicked_amount_3 + 1
        seed_amount += 1

def basket_button_clicked():
    global apple_amount
    global price_basket
    global basket_amount
    global information
    global button_clicked_amount_4
    if (apple_amount - price_basket) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_basket) + " 个苹果 以购买 老爷爷。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 老爷爷。"
        successful_bought_sound()
        apple_amount -= price_basket
        button_clicked_amount_4 += 1
        price_basket += button_clicked_amount_4 + 2
        basket_amount += 1

def tree_button_clicked():
    global apple_amount
    global price_tree
    global tree_amount
    global information
    global button_clicked_amount_5
    if (apple_amount - price_tree) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_tree) + " 个苹果 以购买 苹果树。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 苹果树。"
        successful_bought_sound()
        apple_amount -= price_tree
        button_clicked_amount_5 += 1
        price_tree += button_clicked_amount_5 + 3
        tree_amount += 1

def garden_button_clicked():
    global apple_amount
    global price_garden
    global garden_amount
    global information
    global button_clicked_amount_6
    if (apple_amount - price_garden) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_garden) + " 个苹果 以购买 果园。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 果园。"
        successful_bought_sound()
        apple_amount -= price_garden
        button_clicked_amount_6 += 1
        price_garden += button_clicked_amount_6 + 4
        garden_amount += 1

def town_button_clicked():
    global apple_amount
    global price_town
    global town_amount
    global information
    global button_clicked_amount_7
    if (apple_amount - price_town) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_town) + " 个苹果 以购买 水果镇。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 水果镇。"
        successful_bought_sound()
        apple_amount -= price_town
        button_clicked_amount_7 += 1
        price_town += button_clicked_amount_7 + 5
        town_amount += 1

def country_button_clicked():
    global apple_amount
    global price_country
    global country_amount
    global information
    global button_clicked_amount_8
    if (apple_amount - price_country) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_country) + " 个苹果 以购买 苹果工厂。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 苹果工厂。"
        successful_bought_sound()
        apple_amount -= price_country
        button_clicked_amount_8 += 1
        price_country += button_clicked_amount_8 + 6
        country_amount += 1

def planet_button_clicked():
    global apple_amount
    global price_planet
    global planet_amount
    global information
    global button_clicked_amount_9
    if (apple_amount - price_planet) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_planet) + " 个苹果 以购买 水果银行。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 水果银行。"
        successful_bought_sound()
        apple_amount -= price_planet
        button_clicked_amount_9 += 1
        price_planet += button_clicked_amount_9 + 7
        planet_amount += 1

def wizardtower_button_clicked():
    global apple_amount
    global price_wizardtower
    global wizardtower_amount
    global information
    global button_clicked_amount_10
    if (apple_amount - price_wizardtower) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_wizardtower) + " 个苹果 以购买 魔法巫师塔。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 魔法巫师塔。"
        successful_bought_sound()
        apple_amount -= price_wizardtower
        button_clicked_amount_10 += 1
        price_wizardtower += button_clicked_amount_10 + 8
        wizardtower_amount += 1

def plane_button_clicked():
    global apple_amount
    global price_plane
    global plane_amount
    global information
    global button_clicked_amount_11
    if (apple_amount - price_plane) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_plane) + " 个苹果 以购买 宇宙飞船。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 宇宙飞船。"
        successful_bought_sound()
        apple_amount -= price_plane
        button_clicked_amount_11 += 1
        price_plane += button_clicked_amount_11 + 9
        plane_amount += 1

def hole_button_clicked():
    global apple_amount
    global price_hole
    global hole_amount
    global information
    global button_clicked_amount_12
    if (apple_amount - price_hole) < 0:
        information = "没有足够的苹果。你需要至少 " + str(price_hole) + " 个苹果 以购买 虫洞。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 虫洞。"
        successful_bought_sound()
        apple_amount -= price_hole
        button_clicked_amount_12 += 1
        price_hole += button_clicked_amount_12 + 10
        hole_amount += 1

def timemachine_button_clicked():
    global apple_amount
    global price_timemachine
    global timemachine_amount
    global information
    global button_clicked_amount_13
    if (apple_amount - price_timemachine) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_timemachine) + " 个苹果 以购买 时光机。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 时光机。"
        successful_bought_sound()
        apple_amount -= price_timemachine
        button_clicked_amount_13 += 1
        price_timemachine += button_clicked_amount_13 + 11
        timemachine_amount += 1

def glass_button_clicked():
    global apple_amount
    global price_glass
    global glass_amount
    global information
    global button_clicked_amount_14
    if (apple_amount - price_glass) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_glass) + " 个苹果 以购买 反物质聚光镜。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 反物质聚光镜。"
        successful_bought_sound()
        apple_amount -= price_glass
        button_clicked_amount_14 += 1
        price_glass += button_clicked_amount_14 + 12
        glass_amount += 1

def js_button_clicked():
    global apple_amount
    global price_js
    global js_amount
    global information
    global button_clicked_amount_15
    if (apple_amount - price_js) < 0:
        information = "没有足够的苹果。你需要至少 " + str(
            price_js) + " 个苹果 以购买 JavaScript 控制台。"
        unsuccessful_bought_sound()
    else:
        information = "你购买了 1 个 JavaScript 控制台。"
        successful_bought_sound()
        apple_amount -= price_js
        button_clicked_amount_15 += 1
        price_js += button_clicked_amount_15 + 13
        js_amount += 1

def apple_amount_entry_update():  # 左侧信息栏显示运算
    global apple_amount
    apple_amount_entry.delete(0, "end")
    apple_amount_entry.insert(0, str(apple_amount))
    apple_amount_entry.after(20, apple_amount_entry_update)

def apple_per_click_entry_update():
    global add_per_click
    apple_per_click_entry.delete(0, "end")
    apple_per_click_entry.insert(0, ("+ " + str(add_per_click) + " / click"))
    apple_per_click_entry.after(20, apple_per_click_entry_update)

def apple_per_second_entry_update():
    global auto_add_per_second
    apple_per_second_entry.delete(0, "end")
    apple_per_second_entry.insert(0, ("+ " + str(auto_add_per_second) + " / s"))
    apple_per_second_entry.after(20, apple_per_second_entry_update)

def entry_information_number_23_upgrade():  # 信息网格显示运算
    global sponsor_amount
    entry_information_number_23.delete(0, "end")
    entry_information_number_23.insert(0, str(sponsor_amount))
    entry_information_number_23.after(300, entry_information_number_23_upgrade)

def entry_information_number_33_upgrade():
    global seed_amount
    entry_information_number_33.delete(0, "end")
    entry_information_number_33.insert(0, str(seed_amount))
    entry_information_number_33.after(300, entry_information_number_33_upgrade)

def entry_information_number_43_upgrade():
    global basket_amount
    entry_information_number_43.delete(0, "end")
    entry_information_number_43.insert(0, str(basket_amount))
    entry_information_number_43.after(300, entry_information_number_43_upgrade)

def entry_information_number_53_upgrade():
    global tree_amount
    entry_information_number_53.delete(0, "end")
    entry_information_number_53.insert(0, str(tree_amount))
    entry_information_number_53.after(300, entry_information_number_53_upgrade)

def entry_information_number_63_upgrade():
    global garden_amount
    entry_information_number_63.delete(0, "end")
    entry_information_number_63.insert(0, str(garden_amount))
    entry_information_number_63.after(300, entry_information_number_63_upgrade)

def entry_information_number_73_upgrade():
    global town_amount
    entry_information_number_73.delete(0, "end")
    entry_information_number_73.insert(0, str(town_amount))
    entry_information_number_73.after(300, entry_information_number_73_upgrade)

def entry_information_number_83_upgrade():
    global country_amount
    entry_information_number_83.delete(0, "end")
    entry_information_number_83.insert(0, str(country_amount))
    entry_information_number_83.after(300, entry_information_number_83_upgrade)

def entry_information_number_93_upgrade():
    global planet_amount
    entry_information_number_93.delete(0, "end")
    entry_information_number_93.insert(0, str(planet_amount))
    entry_information_number_93.after(300, entry_information_number_93_upgrade)

def entry_information_number_103_upgrade():
    global wizardtower_amount
    entry_information_number_103.delete(0, "end")
    entry_information_number_103.insert(0, str(wizardtower_amount))
    entry_information_number_103.after(300, entry_information_number_103_upgrade)

def entry_information_number_113_upgrade():
    global plane_amount
    entry_information_number_113.delete(0, "end")
    entry_information_number_113.insert(0, str(plane_amount))
    entry_information_number_113.after(300, entry_information_number_113_upgrade)

def entry_information_number_123_upgrade():
    global hole_amount
    entry_information_number_123.delete(0, "end")
    entry_information_number_123.insert(0, str(hole_amount))
    entry_information_number_123.after(300, entry_information_number_123_upgrade)

def entry_information_number_133_upgrade():
    global timemachine_amount
    entry_information_number_133.delete(0, "end")
    entry_information_number_133.insert(0, str(timemachine_amount))
    entry_information_number_133.after(300, entry_information_number_133_upgrade)

def entry_information_number_143_upgrade():
    global glass_amount
    entry_information_number_143.delete(0, "end")
    entry_information_number_143.insert(0, str(glass_amount))
    entry_information_number_143.after(300, entry_information_number_143_upgrade)

def entry_information_number_153_upgrade():
    global js_amount
    entry_information_number_153.delete(0, "end")
    entry_information_number_153.insert(0, str(js_amount))
    entry_information_number_153.after(300, entry_information_number_153_upgrade)

def entry_information_number_24_upgrade():
    global price_sponsor
    entry_information_number_24.delete(0, "end")
    entry_information_number_24.insert(0, str(price_sponsor))
    entry_information_number_24.after(300, entry_information_number_24_upgrade)

def entry_information_number_34_upgrade():
    global price_seed
    entry_information_number_34.delete(0, "end")
    entry_information_number_34.insert(0, str(price_seed))
    entry_information_number_34.after(300, entry_information_number_34_upgrade)

def entry_information_number_44_upgrade():
    global price_basket
    entry_information_number_44.delete(0, "end")
    entry_information_number_44.insert(0, str(price_basket))
    entry_information_number_44.after(300, entry_information_number_44_upgrade)

def entry_information_number_54_upgrade():
    global price_tree
    entry_information_number_54.delete(0, "end")
    entry_information_number_54.insert(0, str(price_tree))
    entry_information_number_54.after(300, entry_information_number_54_upgrade)

def entry_information_number_64_upgrade():
    global price_garden
    entry_information_number_64.delete(0, "end")
    entry_information_number_64.insert(0, str(price_garden))
    entry_information_number_64.after(300, entry_information_number_64_upgrade)

def entry_information_number_74_upgrade():
    global price_town
    entry_information_number_74.delete(0, "end")
    entry_information_number_74.insert(0, str(price_town))
    entry_information_number_74.after(300, entry_information_number_74_upgrade)

def entry_information_number_84_upgrade():
    global price_country
    entry_information_number_84.delete(0, "end")
    entry_information_number_84.insert(0, str(price_country))
    entry_information_number_84.after(300, entry_information_number_84_upgrade)

def entry_information_number_94_upgrade():
    global price_planet
    entry_information_number_94.delete(0, "end")
    entry_information_number_94.insert(0, str(price_planet))
    entry_information_number_94.after(300, entry_information_number_94_upgrade)

def entry_information_number_104_upgrade():
    global price_wizardtower
    entry_information_number_104.delete(0, "end")
    entry_information_number_104.insert(0, str(price_wizardtower))
    entry_information_number_104.after(300, entry_information_number_104_upgrade)

def entry_information_number_114_upgrade():
    global price_plane
    entry_information_number_114.delete(0, "end")
    entry_information_number_114.insert(0, str(price_plane))
    entry_information_number_114.after(300, entry_information_number_114_upgrade)

def entry_information_number_124_upgrade():
    global price_hole
    entry_information_number_124.delete(0, "end")
    entry_information_number_124.insert(0, str(price_hole))
    entry_information_number_124.after(300, entry_information_number_124_upgrade)

def entry_information_number_134_upgrade():
    global price_timemachine
    entry_information_number_134.delete(0, "end")
    entry_information_number_134.insert(0, str(price_timemachine))
    entry_information_number_134.after(300, entry_information_number_134_upgrade)

def entry_information_number_144_upgrade():
    global price_glass
    entry_information_number_144.delete(0, "end")
    entry_information_number_144.insert(0, str(price_glass))
    entry_information_number_144.after(300, entry_information_number_144_upgrade)

def entry_information_number_154_upgrade():
    global price_js
    entry_information_number_154.delete(0, "end")
    entry_information_number_154.insert(0, str(price_js))
    entry_information_number_154.after(300, entry_information_number_154_upgrade)

def entry_information_number_30_upgrade():
    global value_sponsor
    entry_information_number_30.delete(0, "end")
    entry_information_number_30.insert(0, ("+" + str(value_sponsor * sponsor_amount)) + " / s")
    entry_information_number_30.after(300, entry_information_number_30_upgrade)

def entry_information_number_35_upgrade():
    global value_seed
    entry_information_number_35.delete(0, "end")
    entry_information_number_35.insert(0, ("+" + str(value_seed * seed_amount)) + " / s")
    entry_information_number_35.after(300, entry_information_number_35_upgrade)

def entry_information_number_45_upgrade():
    global value_basket
    entry_information_number_45.delete(0, "end")
    entry_information_number_45.insert(0, ("+" + str(value_basket * basket_amount)) + " / s")
    entry_information_number_45.after(300, entry_information_number_45_upgrade)

def entry_information_number_55_upgrade():
    global value_tree
    entry_information_number_55.delete(0, "end")
    entry_information_number_55.insert(0, ("+" + str(value_tree * tree_amount)) + " / s")
    entry_information_number_55.after(300, entry_information_number_55_upgrade)

def entry_information_number_65_upgrade():
    global value_garden
    entry_information_number_65.delete(0, "end")
    entry_information_number_65.insert(0, ("+" + str(value_garden * garden_amount)) + " / s")
    entry_information_number_65.after(300, entry_information_number_65_upgrade)

def entry_information_number_75_upgrade():
    global value_town
    entry_information_number_75.delete(0, "end")
    entry_information_number_75.insert(0, ("+" + str(value_town * town_amount)) + " / s")
    entry_information_number_75.after(300, entry_information_number_75_upgrade)

def entry_information_number_85_upgrade():
    global value_country
    entry_information_number_85.delete(0, "end")
    entry_information_number_85.insert(0, ("+" + str(value_country * country_amount)) + " / s")
    entry_information_number_85.after(300, entry_information_number_85_upgrade)

def entry_information_number_95_upgrade():
    global value_planet
    entry_information_number_95.delete(0, "end")
    entry_information_number_95.insert(0, ("+" + str(value_planet * planet_amount)) + " / s")
    entry_information_number_95.after(300, entry_information_number_95_upgrade)

def entry_information_number_105_upgrade():
    global value_wizardtower
    entry_information_number_105.delete(0, "end")
    entry_information_number_105.insert(0, ("+" + str(value_wizardtower * wizardtower_amount)) + " / s")
    entry_information_number_105.after(300, entry_information_number_105_upgrade)

def entry_information_number_115_upgrade():
    global value_plane
    entry_information_number_115.delete(0, "end")
    entry_information_number_115.insert(0, ("+" + str(value_plane * plane_amount)) + " / s")
    entry_information_number_115.after(300, entry_information_number_115_upgrade)

def entry_information_number_130_upgrade():
    global value_hole
    entry_information_number_130.delete(0, "end")
    entry_information_number_130.insert(0, ("+" + str(value_hole * hole_amount)) + " / s")
    entry_information_number_130.after(300, entry_information_number_130_upgrade)

def entry_information_number_135_upgrade():
    global value_timemachine
    entry_information_number_135.delete(0, "end")
    entry_information_number_135.insert(0, ("+" + str(value_timemachine * timemachine_amount)) + " / s")
    entry_information_number_135.after(300, entry_information_number_135_upgrade)

def entry_information_number_145_upgrade():
    global value_glass
    entry_information_number_145.delete(0, "end")
    entry_information_number_145.insert(0, ("+" + str(value_glass * glass_amount)) + " / s")
    entry_information_number_145.after(300, entry_information_number_145_upgrade)

def entry_information_number_155_upgrade():
    global value_js
    entry_information_number_155.delete(0, "end")
    entry_information_number_155.insert(0, ("+" + str(value_js * js_amount)) + " / s")
    entry_information_number_155.after(300, entry_information_number_155_upgrade)

def entry_information_information_upgrade():
    entry_information_information.delete(0, "end")
    entry_information_information.insert(0, information)
    entry_information_information.after(300, entry_information_information_upgrade)

def click_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"./sound/click.wav")
    pygame.mixer.music.play(start=0.0)

def window_download():  # 存档下载窗口
    click_sound()
    rootdownload = tk.Tk()
    rootdownload.title("导出存档")
    # noinspection PyTypeChecker
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
    # noinspection PyTypeChecker
    rootupload.resizable(0, 0)

    save_upload_label = tk.Label(rootupload, text="请输入上次游戏保存的字符串以继续游戏！")
    save_upload_label.pack()

    save_upload_entry = tk.Entry(rootupload, width=150, justify='center')
    save_upload_entry.pack()

    def upload():
        click_sound()
        global apple_amount
        global apple_amount_total
        global sponsor_amount
        global seed_amount
        global basket_amount
        global tree_amount
        global garden_amount
        global town_amount
        global country_amount
        global planet_amount
        global wizardtower_amount
        global plane_amount
        global hole_amount
        global timemachine_amount
        global glass_amount
        global js_amount
        global click_time
        global button_clicked_amount_2
        global button_clicked_amount_3
        global button_clicked_amount_4
        global button_clicked_amount_5
        global button_clicked_amount_6
        global button_clicked_amount_7
        global button_clicked_amount_8
        global button_clicked_amount_9
        global button_clicked_amount_10
        global button_clicked_amount_11
        global button_clicked_amount_12
        global button_clicked_amount_13
        global button_clicked_amount_14
        global button_clicked_amount_15
        global price_sponsor
        global price_seed
        global price_basket
        global price_tree
        global price_garden
        global price_town
        global price_country
        global price_planet
        global price_wizardtower
        global price_plane
        global price_hole
        global price_timemachine
        global price_glass
        global price_js

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
    # noinspection PyTypeChecker
    rootabout.resizable(0, 0)

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
        file_open = open("log/log.txt", "r", encoding='utf-8')
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
        file_open = open("log/module.txt", "r", encoding='utf-8')
        file_log = file_open.read()
        file_open.close()

        text_about.delete(1.0, tk.END)
        text_about.insert("insert", file_log)

    button_log = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken', text="更新信息..",command=log_clicked)
    button_log.grid(row=1, column=1)

    blank_1 = tk.Label(button_frame,text=" ")
    blank_1.grid(row=1,column=2)

    button_credit = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken', text="制作者..",command=credit_clicked)
    button_credit.grid(row=1, column=3)

    blank_2 = tk.Label(button_frame,text=" ")
    blank_2.grid(row=1,column=4)

    button_module = tk.Button(button_frame,
                         cursor='hand2',
                         overrelief='sunken',text="使用模块..",command=module_clicked)
    button_module.grid(row=1, column=5)

    frame_text = tk.Frame(rootabout,padx=15,pady=15)
    frame_text.grid(row=0,column=1)

    text_about = tk.Text(frame_text,width=60)
    text_about.pack()

    file_open = open("log/log.txt", "r", encoding='utf-8')
    file_log = file_open.read()
    file_open.close()

    text_about.delete(1.0, tk.END)
    text_about.insert("insert", file_log)

    rootabout.mainloop()

def statistics_text_upgrade():  # 统计信息显示运算
    statistics_text.delete(1.0, tk.END)
    statistics_text.insert("insert", ("现在的苹果数量：" + str(apple_amount) +
                                      "\n总苹果数量：" + str(apple_amount_total) +
                                      "\n总建筑数量：" + str(building_amount) +
                                      "\n点击次数：" + str(click_time)))
    statistics_text.after(300, statistics_text_upgrade)

def upgrade_button_clicked():  # 升级运算
    global apple_amount
    global information
    global upgrade_button_clicked_time
    if (apple_amount - upgrade_price) < 0:
        information = "没有足够的苹果。你需要至少 " + str(int(upgrade_price)) + " 个苹果以升级。"
    else:
        apple_amount -= upgrade_price
        upgrade_button_clicked_time += 1
        information = "你升级至了 Level " + str(upgrade_button_clicked_time + 1) + "！"

def statistics_button_entry_update():
    statistics_button_entry.delete(0, "end")
    statistics_button_entry.insert(0, "Level " + str(upgrade_button_clicked_time + 1) + " 至 Level " + str(
        upgrade_button_clicked_time + 2))
    statistics_button_entry.after(300, statistics_button_entry_update)

def statistics_button_entry_price_update():
    statistics_button_entry_price.delete(0, "end")
    statistics_button_entry_price.insert(0, "价格：" + str(int(upgrade_price)))
    statistics_button_entry_price.after(300, statistics_button_entry_price_update)

def level_progress_bar_update():  # 等级进度条运算
    if level_progress_now == 1:
        level_progress_bar['maximum'] = 12000
        level_progress_bar['value'] = apple_amount_total
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 2:
        level_progress_bar['maximum'] = 48000
        level_progress_bar['value'] = apple_amount_total - 12000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 3:
        level_progress_bar['maximum'] = 140000
        level_progress_bar['value'] = apple_amount_total - 60000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 4:
        level_progress_bar['maximum'] = 800000
        level_progress_bar['value'] = apple_amount_total - 200000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 5:
        level_progress_bar['maximum'] = 4500000
        level_progress_bar['value'] = apple_amount_total - 1000000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 6:
        level_progress_bar['maximum'] = 13000000
        level_progress_bar['value'] = apple_amount_total - 5500000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 7:
        level_progress_bar['maximum'] = 42000000
        level_progress_bar['value'] = apple_amount_total - 18000000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 8:
        level_progress_bar['maximum'] = 140000000
        level_progress_bar['value'] = apple_amount_total - 60000000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 9:
        level_progress_bar['maximum'] = 800000000
        level_progress_bar['value'] = apple_amount_total - 200000000
        level_progress_bar.after(300, level_progress_bar_update)
    elif level_progress_now == 10:
        level_progress_bar['maximum'] = 100000000000
        level_progress_bar['value'] = apple_amount_total - 1000000000
        level_progress_bar.after(300, level_progress_bar_update)
    else:
        pass

def level_progress_label_left_update():
    global left_label
    level_progress_label_left.delete(0, "end")
    level_progress_label_left.insert(0, "Level " + str(level_progress_now))
    level_progress_label_left.after(300, level_progress_label_left_update)

def level_progress_label_right_update():
    global right_label
    level_progress_label_right.delete(0, "end")
    level_progress_label_right.insert(0, "Level " + str(level_progress_now + 1))
    level_progress_label_right.after(300, level_progress_label_right_update)

def root_close():  # 窗口关闭
    root.destroy()
    sys.exit()

root = tk.Tk()  # 主窗口
root.title("Apple Clicker© " + ver)
root.iconphoto(True, tk.PhotoImage(file='./assets/app.png'))
# noinspection PyTypeChecker
root.resizable(0, 0)
root.overrideredirect(False)

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

style = Style(theme='journal')

auto_amount_add_per_second_thread = threading.Thread(target=main_main_operation_logic)  # 主要运算逻辑线程启动
auto_amount_add_per_second_thread.start()

upgrade_price_thread = threading.Thread(target=upgrade_price_logic)
upgrade_price_thread.start()

progress_bar_thread = threading.Thread(target=progress_bar_logic)
progress_bar_thread.start()

achievement_thread = threading.Thread(target=achievement_logic)
achievement_thread.start()

frame_button = tk.Frame(root)
frame_button.grid(row=1, column=2)

button_sponsor = tk.Button(frame_button, text="购买 鼠标指针",
                         cursor='hand2',
                         overrelief='sunken',command=sponsor_button_clicked)  # 建筑购买按钮
button_sponsor.grid(row=2, column=1)
button_seed = tk.Button(frame_button, text="购买 果篮",
                         cursor='hand2',
                         overrelief='sunken',command=seed_button_clicked)
button_seed.grid(row=3, column=1)
button_basket = tk.Button(frame_button, text="购买 老爷爷",
                         cursor='hand2',
                         overrelief='sunken', command=basket_button_clicked)
button_basket.grid(row=4, column=1)
button_tree = tk.Button(frame_button, text="购买 苹果树",
                         cursor='hand2',
                         overrelief='sunken',command=tree_button_clicked)
button_tree.grid(row=5, column=1)
button_garden = tk.Button(frame_button, text="购买 果园",
                         cursor='hand2',
                         overrelief='sunken', command=garden_button_clicked)
button_garden.grid(row=6, column=1)
button_town = tk.Button(frame_button, text="购买 水果镇",
                         cursor='hand2',
                         overrelief='sunken', command=town_button_clicked)
button_town.grid(row=7, column=1)
button_country = tk.Button(frame_button, text="购买 苹果工厂",
                         cursor='hand2',
                         overrelief='sunken',command=country_button_clicked)
button_country.grid(row=8, column=1)
button_planet = tk.Button(frame_button, text="购买 水果银行",
                         cursor='hand2',
                         overrelief='sunken', command=planet_button_clicked)
button_planet.grid(row=9, column=1)
button_wizardtower = tk.Button(frame_button, text="购买 魔法巫师塔",
                         cursor='hand2',
                         overrelief='sunken', command=wizardtower_button_clicked)
button_wizardtower.grid(row=10, column=1)
button_plane = tk.Button(frame_button, text="购买 宇宙飞船",
                         cursor='hand2',
                         overrelief='sunken', command=plane_button_clicked)
button_plane.grid(row=11, column=1)
button_hole = tk.Button(frame_button, text="购买 虫洞",
                         cursor='hand2',
                         overrelief='sunken', command=hole_button_clicked)
button_hole.grid(row=12, column=1)
button_timemachine = tk.Button(frame_button, text="购买 时光机",
                         cursor='hand2',
                         overrelief='sunken', command=timemachine_button_clicked)
button_timemachine.grid(row=13, column=1)
button_glass = tk.Button(frame_button, text="购买 反物质聚光镜",
                         cursor='hand2',
                         overrelief='sunken', command=glass_button_clicked)
button_glass.grid(row=14, column=1)
button_js = tk.Button(frame_button, text="购买 JavaScript 控制台",
                         cursor='hand2',
                         overrelief='sunken', command=js_button_clicked)
button_js.grid(row=15, column=1)

label_2 = tk.Label(frame_button, text="Let these cute cursors help you click and click! ")  # 建筑简介
label_2.grid(row=2, column=2)
label_3 = tk.Label(frame_button, text="These apple seeds of quality can give you 3 apples per second! ")
label_3.grid(row=3, column=2)
label_4 = tk.Label(frame_button, text="Fantastic choice for Sunday family picnic! ")
label_4.grid(row=4, column=2)
label_5 = tk.Label(frame_button, text="Apple trees which harvest all year round! ")
label_5.grid(row=5, column=2)
label_6 = tk.Label(frame_button, text="Now grow apples in the backyard of your house! ")
label_6.grid(row=6, column=2)
label_7 = tk.Label(frame_button, text="A town where everyone grow and eat apples in it! ")
label_7.grid(row=7, column=2)
label_8 = tk.Label(frame_button, text="The streets and alleys are filled with a refreshing fragrance! ")
label_8.grid(row=8, column=2)
label_9 = tk.Label(frame_button, text="People finally discovered organic matter millions of light-years away! ")
label_9.grid(row=9, column=2)
label_10 = tk.Label(frame_button, text="Deep into the unverse to get apples on your spacecraft! ")
label_10.grid(row=10, column=2)
label_11 = tk.Label(frame_button, text="Summon a large amount of apples from wizardtowers! ")
label_11.grid(row=11, column=2)
label_12 = tk.Label(frame_button, text="Access to a lot of apples in a parallel universe! ")
label_12.grid(row=12, column=2)
label_13 = tk.Label(frame_button, text="Go back to the past or future to look for more apples! ")
label_13.grid(row=13, column=2)
label_14 = tk.Label(frame_button, text="Change the antimatter in the universe into apples! ")
label_14.grid(row=14, column=2)
label_15 = tk.Label(frame_button, text="Get endless amount of apples by JavaScript! ")
label_15.grid(row=15, column=2)

frame_left = tk.Frame(root, padx=30)
frame_left.grid(row=1, column=1, rowspan=3)

apple_amount_entry = tk.Entry(frame_left,  # 左侧信息栏
                              justify='center',
                              font=("", "14"),
                              width=16)
apple_amount_entry.pack()
apple_amount_entry.after(10, apple_amount_entry_update)

apple_per_click_entry = tk.Entry(frame_left, width=23)
apple_per_click_entry.pack()
apple_per_click_entry.after(300, apple_per_click_entry_update)

apple_per_second_entry = tk.Entry(frame_left, width=23)
apple_per_second_entry.pack()
apple_per_second_entry.after(300, apple_per_second_entry_update)

apple_img = tk.PhotoImage(file="./assets/app.png")

button_click = tk.Button(frame_left,  # 苹果点击按钮
                         command=click_button_clicked,
                         image=apple_img,
                         cursor='hand2',
                         overrelief='sunken',
                         width=160, height=160)
button_click.pack()

information_label_column_1 = tk.Label(frame_button, text="建筑")  # 顶部
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
entry_information_number_23.after(300, entry_information_number_23_upgrade)

entry_information_number_33 = tk.Entry(frame_button, width=5)
entry_information_number_33.grid(row=3, column=3)
entry_information_number_33.after(300, entry_information_number_33_upgrade)

entry_information_number_43 = tk.Entry(frame_button, width=5)
entry_information_number_43.grid(row=4, column=3)
entry_information_number_43.after(300, entry_information_number_43_upgrade)

entry_information_number_53 = tk.Entry(frame_button, width=5)
entry_information_number_53.grid(row=5, column=3)
entry_information_number_53.after(300, entry_information_number_53_upgrade)

entry_information_number_63 = tk.Entry(frame_button, width=5)
entry_information_number_63.grid(row=6, column=3)
entry_information_number_63.after(300, entry_information_number_63_upgrade)

entry_information_number_73 = tk.Entry(frame_button, width=5)
entry_information_number_73.grid(row=7, column=3)
entry_information_number_73.after(300, entry_information_number_73_upgrade)

entry_information_number_83 = tk.Entry(frame_button, width=5)
entry_information_number_83.grid(row=8, column=3)
entry_information_number_83.after(300, entry_information_number_83_upgrade)

entry_information_number_93 = tk.Entry(frame_button, width=5)
entry_information_number_93.grid(row=9, column=3)
entry_information_number_93.after(300, entry_information_number_93_upgrade)

entry_information_number_103 = tk.Entry(frame_button, width=5)
entry_information_number_103.grid(row=10, column=3)
entry_information_number_103.after(300, entry_information_number_103_upgrade)

entry_information_number_113 = tk.Entry(frame_button, width=5)
entry_information_number_113.grid(row=11, column=3)
entry_information_number_113.after(300, entry_information_number_113_upgrade)

entry_information_number_123 = tk.Entry(frame_button, width=5)
entry_information_number_123.grid(row=12, column=3)
entry_information_number_123.after(300, entry_information_number_123_upgrade)

entry_information_number_133 = tk.Entry(frame_button, width=5)
entry_information_number_133.grid(row=13, column=3)
entry_information_number_133.after(300, entry_information_number_133_upgrade)

entry_information_number_143 = tk.Entry(frame_button, width=5)
entry_information_number_143.grid(row=14, column=3)
entry_information_number_143.after(300, entry_information_number_143_upgrade)

entry_information_number_153 = tk.Entry(frame_button, width=5)
entry_information_number_153.grid(row=15, column=3)
entry_information_number_153.after(300, entry_information_number_153_upgrade)

entry_information_number_24 = tk.Entry(frame_button, width=11)
entry_information_number_24.grid(row=2, column=4)
entry_information_number_24.after(300, entry_information_number_24_upgrade)

entry_information_number_34 = tk.Entry(frame_button, width=11)
entry_information_number_34.grid(row=3, column=4)
entry_information_number_34.after(300, entry_information_number_34_upgrade)

entry_information_number_44 = tk.Entry(frame_button, width=11)
entry_information_number_44.grid(row=4, column=4)
entry_information_number_44.after(300, entry_information_number_44_upgrade)

entry_information_number_54 = tk.Entry(frame_button, width=11)
entry_information_number_54.grid(row=5, column=4)
entry_information_number_54.after(300, entry_information_number_54_upgrade)

entry_information_number_64 = tk.Entry(frame_button, width=11)
entry_information_number_64.grid(row=6, column=4)
entry_information_number_64.after(300, entry_information_number_64_upgrade)

entry_information_number_74 = tk.Entry(frame_button, width=11)
entry_information_number_74.grid(row=7, column=4)
entry_information_number_74.after(300, entry_information_number_74_upgrade)

entry_information_number_84 = tk.Entry(frame_button, width=11)
entry_information_number_84.grid(row=8, column=4)
entry_information_number_84.after(300, entry_information_number_84_upgrade)

entry_information_number_94 = tk.Entry(frame_button, width=11)
entry_information_number_94.grid(row=9, column=4)
entry_information_number_94.after(300, entry_information_number_94_upgrade)

entry_information_number_104 = tk.Entry(frame_button, width=11)
entry_information_number_104.grid(row=10, column=4)
entry_information_number_104.after(300, entry_information_number_104_upgrade)

entry_information_number_114 = tk.Entry(frame_button, width=11)
entry_information_number_114.grid(row=11, column=4)
entry_information_number_114.after(300, entry_information_number_114_upgrade)

entry_information_number_124 = tk.Entry(frame_button, width=11)
entry_information_number_124.grid(row=12, column=4)
entry_information_number_124.after(300, entry_information_number_124_upgrade)

entry_information_number_134 = tk.Entry(frame_button, width=11)
entry_information_number_134.grid(row=13, column=4)
entry_information_number_134.after(300, entry_information_number_134_upgrade)

entry_information_number_144 = tk.Entry(frame_button, width=11)
entry_information_number_144.grid(row=14, column=4)
entry_information_number_144.after(300, entry_information_number_144_upgrade)

entry_information_number_154 = tk.Entry(frame_button, width=11)
entry_information_number_154.grid(row=15, column=4)
entry_information_number_154.after(300, entry_information_number_154_upgrade)

entry_information_number_30 = tk.Entry(frame_button, width=12)
entry_information_number_30.grid(row=2, column=5)
entry_information_number_30.after(300, entry_information_number_30_upgrade)

entry_information_number_35 = tk.Entry(frame_button, width=12)
entry_information_number_35.grid(row=3, column=5)
entry_information_number_35.after(300, entry_information_number_35_upgrade)

entry_information_number_45 = tk.Entry(frame_button, width=12)
entry_information_number_45.grid(row=4, column=5)
entry_information_number_45.after(300, entry_information_number_45_upgrade)

entry_information_number_55 = tk.Entry(frame_button, width=12)
entry_information_number_55.grid(row=5, column=5)
entry_information_number_55.after(300, entry_information_number_55_upgrade)

entry_information_number_65 = tk.Entry(frame_button, width=12)
entry_information_number_65.grid(row=6, column=5)
entry_information_number_65.after(300, entry_information_number_65_upgrade)

entry_information_number_75 = tk.Entry(frame_button, width=12)
entry_information_number_75.grid(row=7, column=5)
entry_information_number_75.after(300, entry_information_number_75_upgrade)

entry_information_number_85 = tk.Entry(frame_button, width=12)
entry_information_number_85.grid(row=8, column=5)
entry_information_number_85.after(300, entry_information_number_85_upgrade)

entry_information_number_95 = tk.Entry(frame_button, width=12)
entry_information_number_95.grid(row=9, column=5)
entry_information_number_95.after(300, entry_information_number_95_upgrade)

entry_information_number_105 = tk.Entry(frame_button, width=12)
entry_information_number_105.grid(row=10, column=5)
entry_information_number_105.after(300, entry_information_number_105_upgrade)

entry_information_number_115 = tk.Entry(frame_button, width=12)
entry_information_number_115.grid(row=11, column=5)
entry_information_number_115.after(300, entry_information_number_115_upgrade)

entry_information_number_130 = tk.Entry(frame_button, width=12)
entry_information_number_130.grid(row=12, column=5)
entry_information_number_130.after(300, entry_information_number_130_upgrade)

entry_information_number_135 = tk.Entry(frame_button, width=12)
entry_information_number_135.grid(row=13, column=5)
entry_information_number_135.after(300, entry_information_number_135_upgrade)

entry_information_number_145 = tk.Entry(frame_button, width=12)
entry_information_number_145.grid(row=14, column=5)
entry_information_number_145.after(300, entry_information_number_145_upgrade)

entry_information_number_155 = tk.Entry(frame_button, width=12)
entry_information_number_155.grid(row=15, column=5)
entry_information_number_155.after(300, entry_information_number_155_upgrade)

frame_upgrade = tk.Frame(root)
frame_upgrade.grid(row=2, column=2)

statistics_text_label = tk.Label(frame_upgrade, text="统计信息")  # 统计信息框
statistics_text_label.grid(row=1, column=1, pady=2)

statistics_text_label = tk.Label(frame_upgrade, text="升级")
statistics_text_label.grid(row=1, column=3, columnspan=2, pady=2, padx=100)

statistics_text = tk.Text(frame_upgrade, height=8, width=40, font=("", 11))
statistics_text.grid(row=2, column=1, rowspan=10)
statistics_text.after(300, statistics_text_upgrade)

statistics_button_2 = tk.Button(frame_upgrade, text="升级..", width=10, height=2,
                         cursor='hand2',
                         overrelief='sunken',command=upgrade_button_clicked)
statistics_button_2.grid(row=2, column=3, rowspan=2, sticky='e')

statistics_button_entry = tk.Entry(frame_upgrade)
statistics_button_entry.grid(row=2, column=4)
statistics_button_entry.after(300, statistics_button_entry_update)

statistics_button_entry_price = tk.Entry(frame_upgrade)
statistics_button_entry_price.grid(row=3, column=4, sticky='n')
statistics_button_entry_price.after(300, statistics_button_entry_price_update)

def time_entry_update():
    time_entry.delete(0, "end")
    time_entry.insert(0, time.asctime(time.localtime(time.time())))
    time_entry.after(300, time_entry_update)

time_entry = tk.Entry(frame_upgrade,justify='center',width=30,borderwidth=0)
time_entry.grid(row=4,column=3,columnspan=2,padx=10)
time_entry.after(300,time_entry_update)

frame_bottom = tk.Frame(root)
frame_bottom.grid(row=3, column=1, columnspan=2)

level_progress_label_left = tk.Entry(frame_bottom, width=7, borderwidth=1, justify='center')  # 等级进度条
level_progress_label_left.grid(row=1, column=0)
level_progress_label_left.after(300, level_progress_label_left_update)

level_progress_bar = tk.ttk.Progressbar(frame_bottom, length=300, orient='horizontal', mode='determinate')
level_progress_bar.grid(row=1, column=1)
level_progress_bar.after(300, level_progress_bar_update)

level_progress_label_right = tk.Entry(frame_bottom, width=7, borderwidth=1, justify='center')
level_progress_label_right.grid(row=1, column=2)
level_progress_label_right.after(300, level_progress_label_right_update)

achievements_information_text = tk.Text(frame_button, width=45, height=31)  # 成就框
achievements_information_text.grid(row=2, column=6, rowspan=13,columnspan=2)

achevement_num_all = 25

def achievement_progress_bar_update():
    achievement_get_num = achievement_1_get + achievement_2_get + achievement_3_get + achievement_4_get + achievement_5_get + achievement_6_get + achievement_7_get + achievement_8_get + achievement_9_get + achievement_10_get + achievement_11_get + achievement_12_get + achievement_13_get + achievement_14_get + achievement_15_get + achievement_16_get + achievement_17_get + achievement_18_get + achievement_19_get + achievement_20_get + achievement_21_get + achievement_22_get + achievement_23_get + achievement_24_get + achievement_25_get + achievement_26_get + achievement_27_get + achievement_28_get + achievement_29_get + achievement_30_get + achievement_31_get + achievement_32_get + achievement_33_get + achievement_34_get + achievement_35_get
    achievement_progress_bar['value'] = achievement_get_num
    achievement_progress_bar.after(300,achievement_progress_bar_update)

def achievement_progress_entry_update():
    achievement_get_num = achievement_1_get + achievement_2_get + achievement_3_get + achievement_4_get + achievement_5_get + achievement_6_get + achievement_7_get + achievement_8_get + achievement_9_get + achievement_10_get + achievement_11_get + achievement_12_get + achievement_13_get + achievement_14_get + achievement_15_get + achievement_16_get + achievement_17_get + achievement_18_get + achievement_19_get + achievement_20_get + achievement_21_get + achievement_22_get + achievement_23_get + achievement_24_get + achievement_25_get + achievement_26_get + achievement_27_get + achievement_28_get + achievement_29_get + achievement_30_get + achievement_31_get + achievement_32_get + achievement_33_get + achievement_34_get + achievement_35_get
    achievement_progress_entry.delete(0, "end")
    achievement_progress_entry.insert(0, str(achievement_get_num) + "/" + str(achevement_num_all))
    achievement_progress_entry.after(500, achievement_progress_entry_update)

achievement_progress_bar = tk.ttk.Progressbar(frame_button, length=300,maximum=achevement_num_all, orient='horizontal', mode='determinate')
achievement_progress_bar.grid(row=15, column=6)
achievement_progress_bar.after(500, achievement_progress_bar_update)

achievement_progress_entry = tk.Entry(frame_button,width=5)
achievement_progress_entry.grid(row=15, column=7)
achievement_progress_entry.after(500,achievement_progress_entry_update)

entry_information_information = tk.Entry(frame_bottom,
                                         width=80,
                                         justify='center')
entry_information_information.grid(row=1, column=4,
                                   ipady=1, pady=5, padx=50)
entry_information_information.after(300, entry_information_information_upgrade)

frame_bottom_left = tk.Frame(frame_bottom)
frame_bottom_left.grid(row=1, column=11,columnspan=2)

bottom_button_download = tk.Button(frame_bottom_left,  # 底部按钮
                                   text="导出存档..",
                                   width=10, height=1, pady=3,
                                   cursor='hand2',
                                   overrelief='sunken',
                                   command=window_download)
bottom_button_download.grid(row=1, column=2, sticky='w')

blank_a = tk.Label(frame_bottom_left, text=" ")
blank_a.grid(row=1, column=3)

bottom_button_upload = tk.Button(frame_bottom_left,
                                 text="导入存档..",
                                 width=10, height=1, pady=3,
                                 cursor='hand2',
                                 overrelief='sunken',
                                 command=window_upload)
bottom_button_upload.grid(row=1, column=4, sticky='w')

blank_b = tk.Label(frame_bottom_left, text=" ")
blank_b.grid(row=1, column=5)

bottom_button_about = tk.Button(frame_bottom_left,
                                text="退出..",
                                width=8, height=1, pady=3,
                                cursor='hand2',
                                overrelief='sunken',
                                command=root_close)
bottom_button_about.grid(row=1, column=6, sticky='w')

menubar = tk.Menu(root, bg="red")
root.config(menu=menubar)

operationMenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="关于..", menu=operationMenu)
operationMenu.add_command(label="关于", command=window_about)

def window_cheat():  # 存档下载窗口
    click_sound()
    rootcheat = tk.Tk()
    rootcheat.title("作弊传送门")
    # noinspection PyTypeChecker
    rootcheat.resizable(0, 0)

    cheat_label = tk.Label(rootcheat, text="作弊而得的苹果尝起来很难吃，不是吗？")
    cheat_label.grid(row=1,column=1,columnspan=3)

    cheat_entry = tk.Entry(rootcheat, width=100, justify='center')
    cheat_entry.grid(row=2,column=1,columnspan=3)

    def cheat_process():
        click_sound()
        global apple_amount
        global apple_amount_total
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
                         cursor='hand2',
                         overrelief='sunken',command=cheat_process)
    save_cheat_button.grid(row=3,column=1)

    blank_cheat = tk.Label(frame_bottom_left, text=" ")
    blank_cheat.grid(row=3,column=2)

    def cheat_close():
        click_sound()
        rootcheat.destroy()

    close_cheat_button = tk.Button(rootcheat, width=10, text="关闭..",
                                  cursor='hand2',
                                  overrelief='sunken', command=cheat_close)
    close_cheat_button.grid(row=3,column=3)

    rootcheat.mainloop()

def window_settings():
    rootsettings = tk.Tk()
    rootsettings.title("游戏设置")
    # noinspection PyTypeChecker
    rootsettings.resizable(0, 0)

    set_frame_1 = tk.Frame(rootsettings)
    set_frame_1.pack()

    set_1_label = tk.Label(set_frame_1,text="音效")
    set_1_label.grid(row=1,column=1)

    def musical_on():
        is_musical_on: int = 1

    def musical_off():
        is_musical_on: int = 0

    r = tk.StringVar()
    radio = tk.Radiobutton(set_frame_1,
                                variable=r,
                                value='1',
                                text='Radio1')
    radio.grid(row=1,column=2)
    radio = tk.Radiobutton(set_frame_1,
                                variable=r,
                                value='2',
                                text='Radio2')
    radio.grid(row=1,column=3)
    print(r.get())

operationMenu.add_command(label="设置", command=window_settings)
operationMenu.add_command(label="传送门", command=window_cheat)

exitMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="退出..", menu=exitMenu)
exitMenu.add_command(label="退出", command=root_close)

root.mainloop()


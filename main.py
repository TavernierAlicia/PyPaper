#PyPaper/main.py

#########################################################################################
#    _    _   ___   _      _       _____  _    _   ___  ______ ______  _____ ______     #
#   | |  | | / _ \ | |    | |     /  ___|| |  | | / _ \ | ___ \| ___ \|  ___|| ___ \    #
#   | |  | |/ /_\ \| |    | |     \ `--. | |  | |/ /_\ \| |_/ /| |_/ /| |__  | |_/ /    #
#   | |/\| ||  _  || |    | |      `--. \| |/\| ||  _  ||  __/ |  __/ |  __| |    /     #
#   \  /\  /| | | || |____| |____ /\__/ /\  /\  /| | | || |    | |    | |___ | |\ \     #
#    \/  \/ \_| |_/\_____/\_____/ \____/  \/  \/ \_| |_/\_|    \_|    \____/ \_| \_|    #
#                                                                                       #
#########################################################################################
                                                                                
#-*- coding:utf-8 -*-
import ctypes
import os
import time
from datetime import datetime
 
#### ~ DEFINE VARIABLES ~ ####

#must select just H&M
morning_time = "00:00"
evening_time = "12:00"
night_time = "19:00"

#convert time
morning_timef =  datetime.strptime(morning_time, "%H:%M")
evening_timef =  datetime.strptime(evening_time, "%H:%M")
night_timef =  datetime.strptime(night_time, "%H:%M")

daypart = "morning"
setimg = "defaultimg"
present_img = "default"

morning_img = os.path.normpath("C:/Users/User/Documents/PyPaper/media/morning.jpg")
evening_img = os.path.normpath("C:/Users/User/Documents/PyPaper/media/evening.jpg")
night_img = os.path.normpath("C:/Users/User/Documents/PyPaper/media/night.jpg")

SPI_SETDESKWALLPAPER = 20

running = True
count = 0

#### ~ PROGRAM ~ ####

while running == True:
    
    #### ~ convert time ~ ####
    now = datetime.now()
    present_time = now.strftime("%H:%M")
    present_timef =  datetime.strptime(present_time, "%H:%M")

    #### ~ define day part ~ ####
    #morning
    if present_timef >= morning_timef and present_timef < night_timef and present_timef < evening_timef:
        daypart = "morning"
        setimg = morning_img

    #night
    elif present_timef > evening_timef and present_timef > morning_timef and present_timef >= night_timef: 
        daypart = "night"
        setimg = night_img 
    
    #evening
    elif present_timef >= evening_timef and present_timef > morning_timef and present_timef < night_timef:
        daypart = "evening"
        setimg = evening_img

    #### ~ change picture ~ ####
    #if good picture is not setted
    if setimg != present_img or count == 0:
        #change wallpaper
        if daypart == "morning" :
            #change for morning
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, setimg, 0)
            present_img = setimg
            print("Wallpaper changed by "+setimg)

        elif daypart == "evening":
            #change for evening
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, setimg, 0)
            present_img = setimg
            print("Wallpaper changed by "+setimg)

        else:
            #change for night
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, setimg, 0)
            present_img = setimg
            print("Wallpaper changed by "+setimg)

    else:
        print("Good picture already here")
        #pass

    count += 1
    time.sleep(60)



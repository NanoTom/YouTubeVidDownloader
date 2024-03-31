from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#this is image recongition
while 1:
    try:
        if pyautogui.locateOnScreen('stickdog.png', region=(175, 305, 800, 800), grayscale = True, confidence = 0.9) != None:
            print("I can see it")
            time.sleep(0.5)
        elif keyboard.is_pressed('q') == True:
            break
        else:
            print("I am unable to see it")
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException:  #i have to use this instead of the if statmet maybe issue in the version
        print("I cant see it")
        time.sleep(0.5)
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#how to make image recognition??

#aimbooster pad location region=(720, 555, 1027, 720)

time.sleep(3)

#rgb of the circle = (255, 219, 195)

def click(x,y):
    print("clicking")
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(720, 555, 1027, 720)) #screenshots the region and saves it here
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))  #cute

            if b==195:
                click(x + 719, y +555)
                time.sleep(0.05)
                break


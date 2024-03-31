from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# Tile 1: X:  641 Y: 1189 RGB: (159, 164, 231)
# Tile 2: X:  789 Y: 1182 RGB: (156, 161, 231)
# Tile 3: X:  916 Y: 1196 RGB: ( 95,  98, 139)
# Tile 4: X: 1094 Y: 1201 RGB: (167, 171, 233)


#this win32api click function:

def click(x,y):
    print("Clicking")
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #idk what is ,0,0
    time.sleep(0.01) #this puases the script for 0.01 seconds if click too fast it can stop clicking
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #this mouse click up

while keyboard.is_pressed('q') == False: #while the user now holding down q
    if pyautogui.pixel(641,900)[0] == 0:
        click(641,900)
    if pyautogui.pixel(789,900)[0] == 0:
        click(789,900)
    if pyautogui.pixel(916,900)[0] == 0:
        click(916,900)
    if pyautogui.pixel(1094,900)[0] == 0:
        click(1094,900)

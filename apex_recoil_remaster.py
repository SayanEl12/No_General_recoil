import time
import win32api
import random
import keyboard
import guns_settings
#from test import *

horizontal_range = 10
min_vertical = 20
max_vertical = 22

min_firerate = 0.03
max_firerate = 0.04

toggle_button = 'num lock'
enabled = False

def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

def get_key():
    if keyboard.is_pressed('ctrl+1'):
        return 1
    elif keyboard.is_pressed('ctrl+2'):
        return 2
    elif keyboard.is_pressed('ctrl+3'):
        return 3

print("Anti-recoil script started!")
if enabled:
    print("Currently ENABLED")
else:
    print("Currently DISABLED")

last_state = False
recoil_type = 0
while True:
    key_down = keyboard.is_pressed(toggle_button)

    if keyboard.is_pressed('ctrl+1'):
        print(1)
        recoil_type = 0
    elif keyboard.is_pressed('ctrl+2'):
        print(2)
        recoil_type = 1
    elif keyboard.is_pressed('ctrl+3'):
        print(3)
        recoil_type = 2

    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")

    if is_mouse_down() and enabled:
        if recoil_type == 0:
            guns_settings.soft_recoil()
        elif recoil_type == 1:
            guns_settings.normal_recoil()
        elif recoil_type == 2:
            guns_settings.heavy_recoil()


    time.sleep(0.001)
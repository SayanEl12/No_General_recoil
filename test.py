import keyboard
import threading
import time
from ctypes import *

import win32api
import win32con
import math

def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

while 1:
    if is_mouse_down():
        windll.user32.mouse_event(0x0001, int(0), int(1))
        time.sleep(0.01)


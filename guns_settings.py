import time
import win32api
import random
from ctypes import *
import threading
def move_mouse(x, y):
    windll.user32.mouse_event(
        c_uint(0x0001),
        c_uint(x),
        c_uint(y),
        c_uint(0),
        c_uint(0)
    )

horizontal_range = 2
min_vertical = 13
max_vertical = 15

min_firerate = 0.03
max_firerate = 0.04

offset_const = 1000

def heavy_recoil():
    horizontal_range = 6
    min_vertical = 27
    max_vertical = 30

    min_value_x = (-horizontal_range * offset_const)
    max_value_x = (horizontal_range * offset_const)
    horizontal_offset = random.uniform(min_value_x, max_value_x) / offset_const

    min_value_y = (min_vertical * offset_const)
    max_value_y = (max_vertical * offset_const)
    vertical_offset = random.randrange(min_value_y, max_value_y, 1) / offset_const

    win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

    time_offset = random.uniform(min_firerate * offset_const, max_firerate * offset_const) / offset_const
    time.sleep(time_offset)

def normal_recoil():
    min_vertical = 13
    max_vertical = 15

    min_value_y = (min_vertical * offset_const)
    max_value_y = (max_vertical * offset_const)
    vertical_offset = random.randrange(min_value_y, max_value_y, 1) / offset_const

    min_value_x = (-horizontal_range * offset_const)
    max_value_x = (horizontal_range * offset_const)
    horizontal_offset = random.uniform(min_value_x, max_value_x) / offset_const

    win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

    time_offset = random.uniform(min_firerate * offset_const, max_firerate * offset_const) / offset_const
    time.sleep(time_offset)

def soft_recoil():
    horizontal_range = 2
    min_vertical = 1
    max_vertical = 4

    min_value_y = (min_vertical * offset_const)
    max_value_y = (max_vertical * offset_const)
    vertical_offset = random.randrange(min_value_y, max_value_y, 1) / offset_const

    min_value_x = (-horizontal_range * offset_const)
    max_value_x = (horizontal_range * offset_const)
    horizontal_offset = random.uniform(min_value_x, max_value_x) / offset_const

    win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

    time_offset = random.uniform(min_firerate * offset_const, max_firerate * offset_const) / offset_const
    time.sleep(time_offset)

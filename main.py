#!python3

import pyautogui as p
import time as t

def CheckBuys():
    for i in range(0,5):
        p.click(1072,409)
        p.click(1395,412)
        p.click(1073,618)
        p.click(1398,614)
        p.click(1064,802)
        p.click(1381,820)
    p.click(806, 516)
    return 

def CheckUpgrades():
    t.sleep(0.5)
    p.click(1152,222)
    p.click(1178,406)
    p.click(1180,597)
    p.click(1183,808)
    p.click(992,217)
    return

i = 0

t.sleep(3)

while True:
    i = i + 1
    if i == 100:
        CheckBuys()
    elif i >= 300:
        CheckUpgrades()
        i = 0
    else:
        p.click(471,633)


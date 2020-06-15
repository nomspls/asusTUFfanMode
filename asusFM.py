#!/usr/bin/env python

import os
from subprocess import run


def getMode():
    logs = run("dmesg | grep -I 'asus_wmi: Set fan'",
                 shell=True, capture_output=True, text=True).stdout
    global currentMode
    try:
        currentMode = logs.split('\n')[-2][-1]
    except:
        currentMode = '0'

def start():
    getMode()
    
    if currentMode == '0':
        os.system("notify-send 'Mode set to BALANCED'")
    elif currentMode == '1':
        os.system("notify-send 'Mode set to OVERBOOST'")
    elif currentMode == '2':
        os.system("notify-send 'Mode set to SILENT'")
    
    # print(currentMode)

start()

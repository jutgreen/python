import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None
if (len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1:
    numMin = 3
else:
    numMin = int(sys.argv[1])
while True:
    x = 0
    while x < numMin:
        time.sleep(60)
        x += 1
    for i in range(0, 1):
        # pyautogui.moveTo(960, i * 4)  # start in top middle of display
        pyautogui.moveTo(1, 1)
        pyautogui.moveTo(1, 1920)
        pyautogui.moveTo(1080, 1920)
        pyautogui.moveTo(1920, 1080)
        pyautogui.moveTo(960, 540)
    for i in range(0, 3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))

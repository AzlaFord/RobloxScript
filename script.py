import pyautogui as key
import time

key.FAILSAFE = False
key.PAUSE = 0.05


time.sleep(0.5)

key.keyDown("x")
time.sleep(2)
key.keyUp("x")
key.press("g")
key.press("g")

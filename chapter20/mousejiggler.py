import pyautogui, random

while True:
    pyautogui.sleep(10)
    pyautogui.moveRel(random.choice((1, -1)), 0)

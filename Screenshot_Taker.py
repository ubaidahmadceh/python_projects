import time
import pyautogui

def take_screenshot():
    time.sleep(5)
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    image = pyautogui.screenshot(name)

take_screenshot()


# pip install pyautogui
# pip install pillow
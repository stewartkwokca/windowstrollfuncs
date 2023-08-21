import pyautogui
from win32api import GetSystemMetrics
from PIL import Image
import helpers
import time
from random import randrange

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)

def logout(alert=False):
    if alert:
        pyautogui.alert(text="YOU'RE TOO DUMB TO USE THIS COMPUTER", title='ERROR', button='LOL')
    pyautogui.hotkey('win', 'd')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('enter')

def fake_broken():
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(w, h)
    im = Image.open("./broken_screen.jpg")
    helpers.showFull(im)

def troll_vid(link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"): # Link for Rickroll
    pyautogui.press('win')
    helpers.enter('run')
    helpers.enter('chrome')
    time.sleep(0.1)
    helpers.enter(link)

def auto_caps():
    while True:
        with pyautogui.hold('shift'):
            time.sleep(randrange(2, 5))
        time.sleep(randrange(2, 5))

def fake_hack(alert=True):
    if alert:
        pyautogui.alert(text="YOU'VE BEEN HACKED", title='WARNING', button='OK')
    pyautogui.hotkey('win', 'r')
    helpers.enter('cmd')
    time.sleep(0.5)
    helpers.enter('color 0A')
    time.sleep(0.5)
    helpers.enter('REM Preparing data transfer to remote location...')
    time.sleep(3)
    helpers.enter('dir/s')
    helpers.enter('REM Data transfer complete.')

def forrest():
    pyautogui.hotkey('win', 'r')
    helpers.enter('cmd')
    time.sleep(0.5)
    helpers.enter('curl ascii.live/forrest')
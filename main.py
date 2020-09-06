import pyautogui
import time
msg = input('enter your message:')
n = int(input('how many time you want to write your message: '))
while n > 0:
    time.sleep(1)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    n = n-1

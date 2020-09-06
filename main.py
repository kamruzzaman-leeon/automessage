import pyautogui
import time
message = 100
while message>0:
    time.sleep(1)
    pyautogui.typewrite('finally i did it.')
    pyautogui.press('enter')
    message = message-1

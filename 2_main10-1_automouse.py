# pip install pyautogui
import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

pyautogui.moveTo(1280,155,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("부산 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

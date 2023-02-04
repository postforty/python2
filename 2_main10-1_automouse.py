# pip install pyautogui
# Pillow 에러 발생시 : pip install Pillow --upgrade
import pyautogui
import time
import pyperclip

# 1차 - 좌표 확인
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

# 2차 - 부산 날씨 이동
pyautogui.moveTo(1280,155,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("부산 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

# 3차 - 화면 캡쳐(1000, 225 / 1655, 630)

start_x = 1000
start_y = 220
end_x = 1655
end_y =630

pyautogui.screenshot(r'auto_img.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
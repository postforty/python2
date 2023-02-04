import pyautogui
import time
import pyperclip

# 1차 - 좌표 확인
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

# 2차 - 크롬 아이콘 캡쳐
# start_x = 540
# start_y = 1165
# end_x = 570
# end_y = 1195

# pyautogui.screenshot('chrome_ico.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))

picPosition = pyautogui.locateOnScreen('chrome_ico.png')
print(picPosition)

pyautogui.center(picPosition)
pyautogui.doubleClick(picPosition)
time.sleep(5)


# 기존 코드
weather = ["서울 날씨", "부산 날씨", "양산 날씨", "김해 날씨", "강원도 날씨", "제주도 날씨"]

addr_x = 1200
addr_y = 60
start_x = 1000
start_y = 220
end_x = 1655
end_y =630

# 1차 - 좌표 확인
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

for w in weather:
    pyautogui.moveTo(addr_x, addr_y, 0.2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(3)

    pyperclip.copy(w)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyautogui.screenshot(f'auto_img_{w}.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
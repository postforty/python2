import pyautogui
import time
import pyperclip

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
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(w)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyautogui.screenshot(f'auto_img_{w}.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
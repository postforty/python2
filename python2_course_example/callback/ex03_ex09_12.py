import time

def timer(pause_second, callback):
    print("타이머가 시작됩니다.")
    print(pause_second, "초 뒤 요청하신 함수가 호출됩니다.")

    time.sleep(pause_second)
    callback()
    print("타이머가 종료됩니다.")

def callback():
    print("요청하신 함수가 호출되었습니다.")


timer(5, callback)
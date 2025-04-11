import threading
import time

def timer(pause_second, callback):
    def task():
        print("타이머가 시작됩니다.")
        print(pause_second, "초 뒤 요청하신 함수가 호출됩니다.")
        time.sleep(pause_second)  # 비동기적 작업의 일부
        callback()
        print("타이머가 종료됩니다.")
    
    threading.Thread(target=task).start()  # 별도의 스레드에서 실행

def callback():
    print("요청하신 함수가 호출되었습니다.")

# 비동기적으로 실행
timer(5, callback)
print("메인 스레드에서 다른 작업 수행 중...")

import time

def task_1():
    print("Task 1 시작")
    time.sleep(2)  # 작업에 2초 소요
    print("Task 1 완료")

def task_2():
    print("Task 2 시작")
    time.sleep(1)  # 작업에 1초 소요
    print("Task 2 완료")

# 직렬 처리
task_1()
task_2()

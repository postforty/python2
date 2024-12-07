import asyncio

async def task_1():
    print("Task 1 시작")
    await asyncio.sleep(2)  # 작업에 2초 소요
    print("Task 1 완료")

async def task_2():
    print("Task 2 시작")
    await asyncio.sleep(1)  # 작업에 1초 소요
    print("Task 2 완료")

# 비동기 처리
async def main():
    await asyncio.gather(task_1(), task_2())  # 동시에 실행

asyncio.run(main())

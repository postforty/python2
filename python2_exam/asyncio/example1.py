# AsyncIO
# 비동기 프로그래밍을 위한 라이브러리

# Blocking I/O : 작업이 완료될 때까지 기다림
# Non-Blocking I/O : 작업이 완료되지 않아도 다음 작업을 수행

# 쓰레드 단점: 디버깅, 자원 접근 시 레이스컨디션(경생상태), 데드락(Dead Lock) 고려해야
# 코루틴 장점: 하나의 루틴만 실행, 락 관리 피료없음, 제어권으로 실행
# 코루틴의 단점: 사용 함수가 비동기로 구현이 되어 있어야 하거나, 또는 직접 비공기로 구현해야 함.

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

urls = [
    'https://www.google.com',
    'https://www.apple.com',
    'https://www.naver.com',
    'https://tistory.com',
]

async def fetch(url, executor):
    print('Thread Name: ', threading.current_thread().getName(), 'Start: ', url)
    result = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name: ', threading.current_thread().getName(), 'Done: ', url)
    return result.read()[0:5]

async def main():
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    result = await asyncio.gather(*futures)

    print('result: ', result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start

    print(f"총 소요 시간: {duration}")

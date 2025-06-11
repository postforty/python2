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

# urlopen을 래핑하여 내부에서 스레드 이름 출력
def blocking_url_fetch(url):
    current_thread_name = threading.current_thread().getName()
    print(f'Actual Worker Thread Name: {current_thread_name} - Starting urlopen for {url}')
    result = urlopen(url)
    print(f'Actual Worker Thread Name: {current_thread_name} - Done urlopen for {url}')
    return result

async def fetch(url, executor):
    print('Asyncio Thread Name (Before executor): ', threading.current_thread().getName(), 'Start: ', url)
    # run_in_executor를 통해 blocking_url_fetch 함수를 워커 스레드에서 실행
    result = await loop.run_in_executor(executor, blocking_url_fetch, url)
    print('Asyncio Thread Name (After executor): ', threading.current_thread().getName(), 'Done: ', url)
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
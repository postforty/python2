import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

async def fetch_url(url, executor):
    # 이 print문은 asyncio 이벤트 루프 스레드에서 실행된다.
    print(f"[Asyncio Thread: {threading.current_thread().getName()}] Starting fetch for {url}")
    
    # urlopen은 블로킹 I/O 작업이므로, ThreadPoolExecutor의 워커 스레드에서 실행하도록 위임한다.
    response = await asyncio.get_event_loop().run_in_executor(executor, urlopen, url)
    
    # urlopen 작업 완료 후, 다시 asyncio 이벤트 루프 스레드에서 실행된다.
    print(f"[Asyncio Thread: {threading.current_thread().getName()}] Done fetch for {url}")
    return response.read()[0:5]

async def main():
    urls = [
        'https://www.google.com',
        'https://www.apple.com',
        'https://www.naver.com',
    ]
    
    # 스레드 풀 생성 (병렬성)
    # max_workers를 통해 동시에 실행될 수 있는 스레드 수를 지정한다.
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            fetch_url(url, executor) # 각 URL에 대해 비동기 fetch 작업 생성
            for url in urls
        ]
        
        # 비동기적으로 모든 작업 완료를 기다린다. (병행성)
        results = await asyncio.gather(*futures)
        print(f"Results: {results}")

if __name__ == "__main__":
    start_time = timeit.default_timer()
    asyncio.run(main()) # Python 3.7+에서 asyncio.run 사용
    duration = timeit.default_timer() - start_time
    print(f"Total time: {duration:.4f} seconds")

# 참고 자료 : https://postforty.tistory.com/578
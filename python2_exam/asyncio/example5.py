import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# urlopen 함수를 래핑하여 실제 실행 스레드 확인
def fetch_url(url):
    current_thread = threading.current_thread().getName()
    print(f"[{current_thread}] Fetching: {url}")
    response = urlopen(url)
    return response.read()[0:5]

async def main():
    urls = [
        'https://www.google.com',
        'https://www.apple.com',
        'https://www.naver.com',
    ]
    
    # 스레드 풀 생성 (병렬성)
    with ThreadPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, fetch_url, url) # I/O 작업을 스레드 풀에 위임
            for url in urls
        ]
        
        # 비동기적으로 모든 작업 완료 대기 (병행성)
        results = await asyncio.gather(*futures)
        print(f"Results: {results}")

if __name__ == "__main__":
    start_time = timeit.default_timer()
    asyncio.run(main()) # Python 3.7+에서 asyncio.run 사용
    duration = timeit.default_timer() - start_time
    print(f"Total time: {duration:.4f} seconds")
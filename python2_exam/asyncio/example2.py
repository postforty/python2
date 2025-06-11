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
from bs4 import BeautifulSoup

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

    soup = BeautifulSoup(result.read(), 'html.parser')

    # 전체 페이지 소스 확인
    # print(soup.prettify())
    result_data = soup.title

    print('Thread Name: ', threading.current_thread().getName(), 'Done: ', url)
    return result_data

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

"""
해당 파이썬 코드는 병행성(Concurrency)과 병렬성(Parallelism) 모두를 활용한다고 볼 수 있다.

## 1. 병행성(Concurrency)
이 코드는 `asyncio` 라이브러리를 사용하여 비동기(Asynchronous) 방식으로 작업을 처리한다. 이는 다음과 같은 특징으로 인해 병행성에 해당한다.

+ `async/await` 문법: `fetch` 함수가 `async`로 정의되어 있고, `await loop.run_in_executor`를 통해 I/O 작업(네트워크 요청)이 완료될 때까지 다른 작업을 수행할 수 있도록 제어권을 넘겨준다.
+ 이벤트 루프: `asyncio.get_event_loop()`를 통해 이벤트 루프가 생성되고, 이 루프는 여러 I/O 바운드 작업을 동시에 관리한다. 한 작업이 I/O 대기 상태에 있을 때, CPU는 다른 작업을 처리할 수 있다.

이는 단일 코어에서도 여러 작업을 동시에 진행하는 것처럼 보이게 하는 병행성의 핵심 개념이다.

## 2. 병렬성(Parallelism)
이 코드는 `concurrent.futures.ThreadPoolExecutor`를 사용하여 병렬성을 구현한다.

+ `ThreadPoolExecutor`: `ThreadPoolExecutor`는 별도의 스레드 풀을 생성하여 작업을 분산 처리한다. `max_workers=10`으로 설정되어 최대 10개의 스레드를 동시에 사용할 수 있다는 의미이다.
+ `run_in_executor`: `loop.run_in_executor(executor, urlopen, url)`는 `urlopen`이라는 블로킹(Blocking) I/O 작업을 메인 스레드에서 직접 수행하지 않고, 스레드 풀의 별도 스레드에서 실행하도록 위임한다. 이로 인해 여러 `urlopen` 작업이 동시에 다른 스레드에서 실행될 수 있다.

이처럼 여러 스레드에서 동시에 작업을 처리함으로써 실제 CPU 코어를 활용하여 물리적으로 동시에 여러 작업을 수행하는 병렬성을 얻게 된다.

## 3. 결론
결론적으로 이 코드는 `asyncio`를 통한 비동기 I/O와 `ThreadPoolExecutor`를 통한 멀티 스레딩을 결합하여, I/O 바운드 작업(네트워크 요청)에 대해 병행성과 병렬성 모두를 활용하여 효율적으로 처리하고 있다. 이는 파이썬의 GIL(Global Interpreter Lock) 때문에 순수한 CPU 바운드 작업의 병렬성은 제한적이지만, I/O 바운드 작업의 경우 스레드를 통해 GIL을 우회하여 병렬 처리가 가능함을 보여주는 좋은 예시이다.

"""
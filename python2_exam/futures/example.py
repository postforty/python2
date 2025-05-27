# Futures 객체를 사용한 동시성 프로그래밍 예제
# 이 예제는 Python의 concurrent.futures 모듈을 사용하여
# 비동기적으로 작업을 실행하는 방법을 보여줍니다.

# futures : 비동기 실행을 위한 고수준 인터페이스(API)를 제공하는 모듈
# concurret.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 --> Promise 개념


# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우의 문제점 방지 위해 GIL 실행, 리소스 전체에 락이 걸림 --> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

import os
import time
from concurrent import futures

WORK_LIST = [1000000, 10000000, 100000000, 1000000000]


def sum_generator(n):
    """주어진 숫자까지의 합을 계산하는 제너레이터 함수"""
    return sum(i for i in range(1, n+1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    # with futures.ThreadPoolExecutor() as executor:  # 멀티 스레드 처리
    with futures.ProcessPoolExecutor() as executor:  # 멀티 프로세스 처리
        result = executor.map(sum_generator, WORK_LIST)

    end_time = time.time() - start_time

    msg = '\n Results: {}, Time: {:.2f}\n'
    # Results: [500000500000, 50000005000000, 5000000050000000, 500000000500000000], Time: 39.13
    print(msg.format(list(result), end_time))


if __name__ == '__main__':
    main()

# 실행할 때 CPU 사용량은 윈도우의 "작업 관리자"에서 확인 가능

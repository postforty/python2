import os
import time


WORK_LIST = [1000000, 10000000, 100000000, 1000000000]


def sum_generator(n):
    """주어진 숫자까지의 합을 계산하는 제너레이터 함수"""
    return sum(i for i in range(1, n+1))


def main():
    start_time = time.time()

    result = []
    for n in WORK_LIST:
        result.append(sum_generator(n))

    end_time = time.time() - start_time

    msg = '\n Results: {}, Time: {:.2f}\n'
    # Results: [500000500000, 50000005000000, 5000000050000000, 500000000500000000], Time: 43.09
    print(msg.format(list(result), end_time))


if __name__ == '__main__':
    main()

# 실행할 때 CPU 사용량은 윈도우의 "작업 관리자"에서 확인 가능

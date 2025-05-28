import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [1000000, 10000000, 100000000, 1000000000]


def sum_generator(n):
    """주어진 숫자까지의 합을 계산하는 제너레이터 함수"""
    return sum(i for i in range(1, n+1))


futures_list = []


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        for work in WORK_LIST:
            # submit() 메서드는 Future 객체를 반환합니다.
            # 이 객체는 비동기 작업의 결과를 나타냅니다.
            future = executor.submit(sum_generator, work)

            futures_list.append(future)
            # 결과를 기다립니다.
            print(f"Result for {work}: {future}")

        # wait() 메서드는 Future 객체의 상태를 확인하고, 완료된 작업의 결과를 (설정한 시간 내에 끝나는 결과에 대해 한번에) 반환합니다.
        # result = wait(futures_list, timeout=7)
        # as_completed() 메서드는 Future 객체의 결과가 준비되는 대로(먼저 끝나는 대로) 반환(yield)합니다.
        result = as_completed(futures_list, timeout=7)

        print('Completed Tasks:', result.done)
        print('Pending ones after waiting for 7seconds:', result.not_done)
        print([future.result() for future in result.done])

    end_time = time.time() - start_time

    msg = '\nTime: {:.2f}\n'
    print(msg.format(end_time))


if __name__ == '__main__':
    main()

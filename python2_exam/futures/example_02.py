import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

WORK_LIST = [1000000, 10000000, 100000000, 1000000000]


def sum_generator(n):
    """주어진 숫자까지의 합을 계산하는 제너레이터 함수"""
    result = sum(i for i in range(1, n+1))
    end_times[n] = time.time()
    return result


futures_list = []
start_times = {}
end_times = {}


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        for work in WORK_LIST:
            # submit() 메서드는 Future 객체를 반환합니다.
            # 이 객체는 비동기 작업의 결과를 나타냅니다.
            start_times[work] = time.time()
            future = executor.submit(sum_generator, work)

            futures_list.append(future)
            # 결과를 기다립니다.
            print(f"Result for {work}: {future}")

        # wait() 메서드는 Future 객체의 상태를 확인하고, 완료된 작업의 결과를 (설정한 시간 내에 끝나는 결과에 대해 한번에) 반환합니다.
        # result = wait(futures_list, timeout=7)
        # as_completed() 메서드는 Future 객체의 결과가 준비되는 대로(먼저 끝나는 대로) 반환(yield)합니다.
        completed_order = []
        result = as_completed(futures_list, timeout=7)

        for future in result:
            work = None
            for w, f in start_times.items():
                if futures_list[list(start_times.keys()).index(w)] == future:
                    work = w
                    break
            completed_order.append(work)
            logging.info(f"Result {work}: {future.result()}")

        print('Completed Tasks:', result.done)
        print('Pending ones after waiting for 7seconds:', result.not_done)

        sorted_works = sorted(end_times, key=end_times.get)
        print("Completed Order (as_completed):", completed_order)
        print("Completed Order (by end time):", sorted_works)

        if completed_order == sorted_works:
            print("as_completed() works correctly!")
        else:
            print("as_completed() does NOT work correctly!")

    end_time = time.time() - start_time

    msg = '\nTime: {:.2f}\n'
    print(msg.format(end_time))


if __name__ == '__main__':
    main()

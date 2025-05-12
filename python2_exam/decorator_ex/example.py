import time

# 클로저
def perf_clock(func):
    def perf_clocked(*args):
        start_time = time.perf_counter() # 작업에 소요되는 시간을 측정 메서드()
        result = func(*args)
        end_time = time.perf_counter() - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print(f'{end_time}, {name}, {arg_str}, {result}')
        
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)

print(non_deco1(2))
print(non_deco2(1,2,3,4,5))

print("---")

# 데코레이터 사용
@perf_clock # perf_clock를 장식
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

print(time_func(2))
print(sum_func(1,2,3,4,5))
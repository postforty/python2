# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 스레도 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티스레드
# yield : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 스레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생
# 파이선 3.5 이상에서는 def -> async, yield -> await 가능

from inspect import getgeneratorstate


def coroutine1():
    print('>>> coroutine stated.')
    i = yield
    print(f">>> coroutine received : {i}")


# 코루틴 예제1
cr1 = coroutine1()
print(cr1, type(cr1))
# <generator object coroutine1 at 0x000001DDA9D8D970> <class 'generator'>
# yield 지점까지 서브루틴 수행
next(cr1)  # >>> coroutine stated.
# 기본값 Node
# next(cr1)  # coroutine received : None
# 값 전송
# next() 호출 후 send() 호출 가능
# cr1.send(100)  # coroutine received : 100

print()
print()

# 코루틴 예제2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 지점에서 대기 상태
# GEN_CLOSED : 종료 상태


def coroutine2(x):
    print(f'>>> coroutine2 started : {x}')
    y = yield x
    print(f'>>> coroutine2 received : {y}')
    z = yield x + y
    print(f'>>> coroutine2 received : {z}')


cr2 = coroutine2(10)
print(getgeneratorstate(cr2))  # GEN_CREATED
print(next(cr2))
print(cr2.send(100))

print()
print()

# 코루틴 예제3
# 중첩 코루틴 처리


def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))  # StopIteration

t1 = generator1()
print(list(t1))  # ['A', 'B', 1, 2, 3]


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t2 = generator2()
print(list(t2))  # ['A', 'B', 1, 2, 3]

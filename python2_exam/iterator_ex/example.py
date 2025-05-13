# 이터레이터(iterator)
# 파이썬의 반복 가능한(iterable) 타입
# collections, string, list, dict, set, tuple, unpacking, *args...

from collections import abc

s = "abcde"

t = iter(s)

# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t)) # StopIteration

while True:
    try:
        print(next(t))
    except StopIteration:
        break

# 반복형 확인
print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

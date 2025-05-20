# Generator 중요 클래스

import itertools

# 1부터 시작해서 2.5씩 증가
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

print("---")

# 1000이하 까지 1부터 시작해서 2.5씩 증가
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))
for v in gen2:
    print(v)

print("---")

# 필터 반대
# 3 미만 값을 제외
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v, end=" ")  # 3 4 5

print("\n---")

# 누적 합계
gen4 = itertools.accumulate([1, 2, 3, 4, 5])
for v in gen4:
    print(v, end=" ")  # 1 3 6 10 15

print("\n---")

# 연결(체이닝)
# 이터러블 객체의 연결
gen5 = itertools.chain('ABCDE', [1, 2, 3, 4, 5])
print(list(gen5))  # ['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]

gen6 = itertools.chain(enumerate('abcde'))
print(list(gen6))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

print("---")

# 개별
# 개별 튜플로 분리
gen7 = itertools.product('abcde')
print(list(gen7))  # [('a',), ('b',), ('c',), ('d',), ('e',)]
# repeat 크기의 모든 경우의 수
gen7 = itertools.product('ab', repeat=3)
print(list(gen7))
# [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a'), ('a', 'b', 'b'), ('b', 'a', 'a'), ('b', 'a', 'b'), ('b', 'b', 'a'), ('b', 'b', 'b')]

print("---")

# 그룹화
gen8 = itertools.groupby('abcaabbbc')
for chr, group in gen8:
    print(chr, list(group))

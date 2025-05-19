# 병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 해결할 수 있음
# 병렬성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator
# 병행성
def generator_ex1():
    print('Start')
    yield ('네이버 페이지 크롤링')
    print('Continue')
    yield ('구글 페이지 크롤링')
    print('End')


temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))  # StopIteration

for v in generator_ex1():
    print(v)
    # break

temp2 = [x * 3 for x in generator_ex1()]  # list
print(type(temp2))
temp3 = (x * 3 for x in generator_ex1())  # generator
print(type(temp3))

for i in temp2:
    print(i)
"""
네이버 페이지 크롤링네이버 페이지 크롤링네이버 페이지 크롤링
구글 페이지 크롤링구글 페이지 크롤링구글 페이지 크롤링
"""

for i in temp3:
    print(i)
"""
Start
네이버 페이지 크롤링네이버 페이지 크롤링네이버 페이지 크롤링
Continue
구글 페이지 크롤링구글 페이지 크롤링구글 페이지 크롤링
End
"""

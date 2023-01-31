import random

ran_num = random.randint(1, 100)

# print(ran_num)

count = 1

while True:
    num = int(input("1~100 사이의 숫자를 입력하세요: "))

    if num > ran_num:
        print("다운")
    elif num < ran_num:
        print("업")
    elif num == ran_num:
        print(f'정답입니다. {count}회 만에 맞췄습니다.')
        break

    count += 1

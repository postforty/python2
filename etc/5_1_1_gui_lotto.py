import random

lotto_num = range(1, 46)

for i in range(5):
    print(random.sample(lotto_num, 6)) # random.sample는 중복되지 않는 요소를 반환. 반면 random.choice는 요소가 중복될 수 있음.

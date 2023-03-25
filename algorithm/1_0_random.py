import random

result =  []
while True:
    num = random.randint(1, 45)

    # [풀이1]
    # if len(result) == 0:
    #     result.append(num)
    # try:
    #     result.index(num)
    # except:
    #     result.append(num)
    # else:
    #     pass
    # finally:
    #     if len(result) == 6:
    #         break

    # [풀이2]
    if num in result:
        continue
    else:
        result.append(num)

    if len(result) == 6:
        break

print(result)
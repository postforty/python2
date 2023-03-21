import random

result =  []
while True:
    num = random.randint(1, 45)
    if len(result) == 0:
        result.append(num)
    try:
        result.index(num)
    except:
        result.append(num)
    else:
        pass
    finally:
        if len(result) == 6:
            break

print(result)
print('2자리 양수를 입력하세요.')

while True:
    num = int(input('값을 입력하세요 : '))
    if not(num < 10 or num > 99):
    # if num >= 10 and num <= 99:
        break

print(f'입력받은 양수는 {num}입니다.')
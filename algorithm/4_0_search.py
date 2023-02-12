# 코리아 전자 매장에는 부품 N개가 있다.
# 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 손님이 문의한 부품 M개의 종류가 가게에 있는 부품인지 확인하는 프로그램을 작성하라!

# 가게에 있는 부품
# N = 5
# [9, 5, 3, 9, 1]

# 손님이 요청한 부품
# M = 3
# [3, 1, 2]

# 입력시 공백으로 구분
# 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no 출력

n = int(input())

items = set(map(int, input().split()))

m = int(input())

search_items = list(map(int, input().split()))

for i in search_items:
    if i in items:
        print('yes', end=' ')
    else:
        print('no', end=' ')
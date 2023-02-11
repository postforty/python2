# N명의 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
# - 첫 번째 줄에 학생의 수 N을 입력
# - 두 번째 줄 부터 학생 이름, 성적 입력(이름과 성적을 공백으로 구분)

n = int(input('학생 수 N명을 입력하세요 : '))

name = []
score = []
for i in range(n):
    input_data = input("학생 이름, 성적을 입력하세요(공백으로 구분): ").split()
    name.append((input_data[0]))
    score.append((int(input_data[1])))

print(name)
print(score)

# arr = sorted(arr, key=lambda x: x[1])
# # arr = sorted(arr, key=lambda x: x[1], reverse=True)

# print("성적이 낮은 순: ", end='')

# for i in arr:
#     print(i[0], end=', ')


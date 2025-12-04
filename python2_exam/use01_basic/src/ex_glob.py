"""glob 모듈 실습 예제"""
import glob
import os

# 실습용 테스트 파일들 생성
print("=== 1. 테스트 파일 생성 ===")
test_files = [
    "20241201_1.txt",
    "20241201_2.txt",
    "20241202_1.txt",
    "20231225_1.txt",
    "diary.txt",
    "note_20241201.txt",
]

for filename in test_files:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"테스트 파일: {filename}")
    print(f"생성: {filename}")

print("\n=== 2. glob 패턴 매칭 실습 ===")

# 패턴 1: 모든 .txt 파일
print("\n[패턴: *.txt]")
print("결과:", glob.glob("*.txt"))

# 패턴 2: YYYYMMDD_N.txt 형식 (8자리 숫자 + _ + 임의 문자 + .txt)
print("\n[패턴: [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_*.txt]") # *는 와일드카드 문자
print("설명: 8자리 숫자로 시작하고 _가 있는 txt 파일")
result = glob.glob("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_*.txt")
print("결과:", sorted(result))

# 패턴 3: 2024년 12월 파일만
print("\n[패턴: 202412*_*.txt]")
print("결과:", sorted(glob.glob("202412*_*.txt")))

# 패턴 4: 숫자로 시작하는 모든 파일
print("\n[패턴: [0-9]*.txt]")
print("결과:", sorted(glob.glob("[0-9]*.txt")))

print("\n=== 3. glob 패턴 문법 설명 ===")
print("""
* : 임의의 문자열 (0개 이상)
? : 임의의 한 문자
[0-9] : 0부터 9까지의 숫자 중 하나
[a-z] : a부터 z까지의 소문자 중 하나
[abc] : a, b, c 중 하나

예시:
- *.txt : 모든 txt 파일
- test?.txt : test1.txt, testA.txt 등
- [0-9][0-9].txt : 01.txt, 99.txt 등 (2자리 숫자)
- 2024*.txt : 2024로 시작하는 txt 파일
""")

print("\n=== 4. 정리 (cleanup) ===")
for filename in test_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"삭제: {filename}")

print("\n실습 완료!")

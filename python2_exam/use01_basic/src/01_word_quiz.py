# 단어장 퀴즈
import random

def main():
    # 단어장 딕셔너리 초기화
    word_book = {}
    
    while True:
        print("\n--- 영어 단어장 (Word Book) ---")
        print("1. 단어 추가")
        print("2. 단어 검색")
        print("3. 단어 퀴즈")
        print("4. 전체 목록 보기")
        print("5. 종료")
        
        choice = input("메뉴를 선택하세요: ")
        
        if choice == '1':
            word = input("영어 단어 입력: ").strip()
            if not word:
                print("단어를 입력해주세요.")
                continue
            meaning = input("뜻 입력: ").strip()
            word_book[word] = meaning
            print(f"'{word}' 단어가 추가되었습니다.")
            
        elif choice == '2':
            word = input("검색할 단어 입력: ").strip()
            if word in word_book:
                print(f"뜻: {word_book[word]}")
            else:
                print("등록되지 않은 단어입니다.")
                
        elif choice == '3':
            if not word_book:
                print("저장된 단어가 없습니다. 먼저 단어를 추가해주세요.")
                continue
            
            # 저장된 단어 중 하나를 랜덤으로 선택
            quiz_word = random.choice(list(word_book.keys()))
            print(f"문제: '{quiz_word}'의 뜻은 무엇일까요?")
            answer = input("정답 입력: ").strip()
            
            if answer == word_book[quiz_word]:
                print("정답입니다! 👏")
            else:
                print(f"틀렸습니다. 정답은 '{word_book[quiz_word]}'입니다.")
        
        elif choice == '4':
            print("\n[ 저장된 단어 목록 ]")
            if not word_book:
                print("저장된 단어가 없습니다.")
            else:
                for w, m in word_book.items():
                    print(f"- {w} : {m}")
                
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()

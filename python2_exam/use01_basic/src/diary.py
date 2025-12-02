import os
import datetime
import glob

def get_diary_files():
    """일기 파일 목록을 가져옵니다 (YYYYMMDD_N.txt 패턴)."""
    return sorted(glob.glob("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_*.txt"))

def write_diary():
    """새로운 일기를 작성합니다."""
    content = input("내용을 입력하세요: ")

    today = datetime.datetime.now().strftime("%Y%m%d")
    count = 1
    while True:
        filename = f"{today}_{count}.txt"
        if not os.path.exists(filename):
            break
        count += 1
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"일기가 {filename}에 저장되었습니다.")

def read_diary():
    """모든 일기를 읽어서 출력합니다."""
    files = get_diary_files()
    if not files:
        print("저장된 일기가 없습니다.")
        return

    print("\n--- 일기 목록 ---")
    for filename in files:
        print(f"\n[파일: {filename}]")
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read().strip())
    print("\n-----------------")

def update_diary():
    """특정 파일의 일기를 수정합니다."""
    files = get_diary_files()
    if not files:
        print("수정할 일기가 없습니다.")
        return

    print("\n--- 수정 가능한 일기 목록 ---")
    for filename in files:
        print(filename)
    
    target_file = input("\n수정할 파일명을 입력하세요 (예: 20251202_1.txt): ")
    
    if target_file not in files:
        print("해당 파일을 찾을 수 없습니다.")
        return

    with open(target_file, "r", encoding="utf-8") as f:
        print(f"현재 내용: {f.read().strip()}")
    
    new_content = input("새로운 내용을 입력하세요: ")
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("일기가 수정되었습니다.")

def delete_diary():
    """특정 파일의 일기를 삭제합니다."""
    files = get_diary_files()
    if not files:
        print("삭제할 일기가 없습니다.")
        return

    print("\n--- 삭제 가능한 일기 목록 ---")
    for filename in files:
        print(filename)
    
    target_file = input("\n삭제할 파일명을 입력하세요: ")
    
    if target_file not in files:
        print("해당 파일을 찾을 수 없습니다.")
        return
        
    os.remove(target_file)
    print("일기가 삭제되었습니다.")

def main():
    while True:
        print("\n1. 일기 쓰기")
        print("2. 일기 읽기")
        print("3. 일기 수정")
        print("4. 일기 삭제")
        print("5. 종료")
        
        choice = input("선택: ")
        
        if choice == '1':
            write_diary()
        elif choice == '2':
            read_diary()
        elif choice == '3':
            update_diary()
        elif choice == '4':
            delete_diary()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()

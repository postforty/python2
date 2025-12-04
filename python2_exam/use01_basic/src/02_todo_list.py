# 초보자를 위한 파이썬 Todo List 예제
# 리스트와 딕셔너리를 사용하여 할 일 목록을 관리하는 프로그램입니다.

def print_menu():
    """사용 가능한 메뉴를 출력합니다."""
    print("\n" + "=" * 30)
    print("   Todo List 관리 프로그램")
    print("=" * 30)
    print("1. 할 일 목록 보기")
    print("2. 할 일 추가하기")
    print("3. 할 일 완료하기")
    print("4. 할 일 삭제하기")
    print("5. 종료하기")
    print("=" * 30)

def add_task(todos):
    """새로운 할 일을 추가합니다."""
    title = input("\n추가할 할 일 내용을 입력하세요: ")
    if title.strip() == "":
        print("내용이 입력되지 않았습니다.")
        return
    
    # 할 일은 딕셔너리 형태로 저장합니다.
    # title: 할 일 내용, done: 완료 여부 (True/False)
    new_todo = {"title": title, "done": False}
    todos.append(new_todo)
    print(f"'{title}' 할 일이 추가되었습니다.")

def view_tasks(todos):
    """현재 할 일 목록을 출력합니다."""
    print("\n[ 할 일 목록 ]")
    if not todos:
        print("등록된 할 일이 없습니다.")
        return

    # enumerate를 사용하여 인덱스와 값을 함께 가져옵니다.
    # 인덱스는 0부터 시작하지만, 사용자에게는 1부터 보여줍니다.
    for index, todo in enumerate(todos, start=1):
        status = "[x]" if todo["done"] else "[ ]"
        print(f"{index}. {status} {todo['title']}")

def complete_task(todos):
    """할 일을 완료 상태로 변경합니다."""
    view_tasks(todos)
    if not todos:
        return

    try:
        index = int(input("\n완료할 할 일의 번호를 입력하세요: "))
        # 사용자 입력은 1부터 시작하므로 리스트 인덱스(0부터 시작)로 변환하려면 1을 뺍니다.
        if 1 <= index <= len(todos):
            todo = todos[index - 1]
            if todo["done"]:
                print("이미 완료된 할 일입니다.")
            else:
                todo["done"] = True
                print(f"'{todo['title']}' 할 일이 완료되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

def delete_task(todos):
    """할 일을 목록에서 삭제합니다."""
    view_tasks(todos)
    if not todos:
        return

    try:
        index = int(input("\n삭제할 할 일의 번호를 입력하세요: "))
        if 1 <= index <= len(todos):
            removed_todo = todos.pop(index - 1)
            print(f"'{removed_todo['title']}' 할 일이 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

def main():
    """프로그램의 메인 로직입니다."""
    # 할 일 목록을 저장할 리스트
    todos = []

    while True:
        print_menu()
        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            view_tasks(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            complete_task(todos)
        elif choice == '4':
            delete_task(todos)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1번부터 5번까지의 숫자를 입력해주세요.")

# 이 파일이 직접 실행될 때만 main() 함수를 호출합니다.
if __name__ == "__main__":
    main()

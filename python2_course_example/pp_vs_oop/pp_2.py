# --- Data (Global) ---
students_db = [] # 학생 정보를 저장할 리스트 (전역 데이터)
                 # 각 요소는 학생 정보를 담는 딕셔너리

# --- Procedures (Functions) ---

# == 학생 등록 함수 분리 (유형별) ==
# 이유: 대학원생은 'thesis_topic' 이라는 추가 정보가 필요하므로,
#      하나의 함수로 처리하기 복잡해져 분리 선택 (불편함 1: 함수 분리 또는 복잡한 파라미터 처리 필요)
def register_regular_student(name, grade):
    """일반 학생을 등록하는 절차"""
    global students_db
    print(f"\n[절차 시작] 일반 학생 등록: 이름={name}, 학년={grade}")
    # 중복 체크 (간단화) - 이 로직은 아래 함수와 중복됨 (문제점 1: 코드 중복)
    for student in students_db:
        if student['name'] == name:
            print(f"[오류] 이미 등록된 학생입니다: {name}")
            return

    # 학생 정보를 딕셔너리로 구성 (유형 정보 추가)
    student_data = {
        'name': name,
        'grade': grade,
        'type': 'regular', # 학생 유형 명시
        'scores': {},
        # 'thesis_topic': None # 이 키를 넣을지 말지 일관성 유지 어려움 (문제점 2: 데이터 구조 복잡/불일치)
    }
    students_db.append(student_data)
    print(f"[등록 완료] {name} 일반 학생 정보가 추가되었습니다.")
    print(f"현재 학생 수: {len(students_db)}명")

def register_graduate_student(name, grade, thesis_topic):
    """대학원생을 등록하는 절차"""
    global students_db
    print(f"\n[절차 시작] 대학원생 등록: 이름={name}, 학년={grade}, 주제={thesis_topic}")
    # 중복 체크 (간단화) - 위 함수와 코드 중복 (문제점 1: 코드 중복)
    for student in students_db:
        if student['name'] == name:
            print(f"[오류] 이미 등록된 학생입니다: {name}")
            return

    # 학생 정보를 딕셔너리로 구성 (유형 정보 및 추가 정보 포함)
    student_data = {
        'name': name,
        'grade': grade,
        'type': 'graduate', # 학생 유형 명시
        'scores': {},
        'thesis_topic': thesis_topic # 대학원생 고유 정보 추가
    }
    students_db.append(student_data)
    print(f"[등록 완료] {name} 대학원생 정보가 추가되었습니다.")
    print(f"현재 학생 수: {len(students_db)}명")


def assign_score(student_name, subject, score):
    """학생에게 성적을 부여하는 절차 (학생 유형에 거의 영향받지 않음)"""
    global students_db
    print(f"\n[절차 시작] 성적 부여: 학생={student_name}, 과목={subject}, 점수={score}")
    student_found = False
    for student in students_db: # student는 딕셔너리
        if student['name'] == student_name:
            student['scores'][subject] = score
            print(f"[성적 입력 완료] {student_name} 학생의 {subject} 과목 점수가 {score}점으로 입력되었습니다.")
            student_found = True
            break
    if not student_found:
        print(f"[오류] {student_name} 학생을 찾을 수 없습니다.")

# == 평균 계산 함수 추가 ==
# 이유: 평균 계산 로직이 필요해짐. 이 로직은 학생 데이터와 분리되어 있음.
def calculate_average_score(student_scores_dict):
    """학생의 성적 딕셔너리를 받아 평균을 계산하는 '별도의' 절차"""
    if not student_scores_dict:
        return 0.0
    return sum(student_scores_dict.values()) / len(student_scores_dict)

# == 정보 출력 함수 수정 (가장 큰 변화 및 문제 발생 지점) ==
def print_school_report():
    """전체 학생의 정보를 '유형에 따라 다르게' 출력하는 절차"""
    global students_db
    print("\n[절차 시작] 전체 학생 정보 출력")
    print("=" * 50)
    print("       < 전체 학생 현황 (절차지향 - 수정됨) >")
    print("=" * 50)

    if not students_db:
        print("등록된 학생이 없습니다.")
        print("=" * 50)
        return

    # 학생 데이터베이스(리스트)를 순회
    for student_dict in students_db: # student_dict는 학생 정보를 담은 딕셔너리
        # 평균 계산 함수를 호출하여 결과 받기
        avg_score = calculate_average_score(student_dict['scores'])

        # === 학생 유형('type' 키)에 따라 분기하여 처리 ===
        # (문제점 3: 거대한 조건문 블록 발생, OCP 위반)
        student_type = student_dict.get('type', 'unknown') # 타입 키가 없을 경우 대비

        if student_type == 'regular':
            # --- 일반 학생 정보 출력 로직 ---
            print(f" 이름: {student_dict['name']} ({student_dict['grade']}학년) [타입: 일반학생]")
            if student_dict['scores']:
                print("  * 성적:")
                for subject, score in student_dict['scores'].items():
                    print(f"    - {subject}: {score}점")
                print(f"  * 평균 점수: {avg_score:.2f}점") # 평균 점수 출력
            else:
                print("  * 등록된 성적이 없습니다.")

        elif student_type == 'graduate':
            # --- 대학원생 정보 출력 로직 ---
            print(f" 이름: {student_dict['name']} ({student_dict['grade']}학년) [타입: 대학원생]")
            if student_dict['scores']:
                print("  * 성적:")
                for subject, score in student_dict['scores'].items():
                    print(f"    - {subject}: {score}점")
                print(f"  * 평균 점수: {avg_score:.2f}점") # 평균 점수 출력
            else:
                print("  * 등록된 성적이 없습니다.")
            # 대학원생만 논문 주제 출력 (키 존재 여부 확인 필요 가능성 있음)
            print(f"  * 논문 주제: {student_dict.get('thesis_topic', 'N/A')}") # .get()으로 안전하게 접근

        else: # 만약 새로운 타입이 추가되면? 이 함수를 계속 수정해야 함!
            # --- 알 수 없는 타입 처리 ---
            print(f" 이름: {student_dict['name']} ({student_dict['grade']}학년) [타입: {student_type}]")
            print("  * 알 수 없는 학생 타입 데이터입니다.")

        print("-" * 30) # 학생 간 구분선

    print("=" * 50)
    print("[출력 완료]")


# --- 프로그램 실행 흐름 (Main) ---

print("=== 학교 관리 프로그램 시작 (절차지향 방식 - 수정됨) ===")

# 유형별 등록 함수 사용
register_regular_student("김민준", 1)
register_regular_student("이서연", 2)
register_graduate_student("박지성", 5, "머신러닝 기반 자연어 처리") # 대학원생 등록

# 성적 부여 (assign_score는 수정 없이 사용 가능)
assign_score("김민준", "파이썬 기초", 90)
assign_score("이서연", "객체지향 설계", 85)
assign_score("박지성", "딥러닝 연구", 95)
assign_score("김민준", "웹 프로그래밍", 88)
assign_score("박지성", "컴퓨터 비전 세미나", 100)

# 전체 학생 정보 출력 (수정된 함수 호출)
print_school_report()

print("\n=== 학교 관리 프로그램 종료 ===")
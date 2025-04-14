# 절차적 프로그래밍(Procedure Programming)

# --- 데이터 영역 ---
# 학생 정보를 저장할 리스트 (전역 변수로 사용)
students_db = []

# --- 절차 (함수) 영역 ---

def register_student(name, grade):
  """학생을 등록하는 절차"""
  global students_db # 전역 변수인 students_db를 사용하겠다고 명시
  print(f"\n[절차 시작] 학생 등록: 이름={name}, 학년={grade}")

  # 간단한 중복 체크 (이름 기준) - 실제로는 더 정교해야 함
  for student in students_db:
    if student['name'] == name:
      print(f"[오류] 이미 등록된 학생입니다: {name}")
      return # 절차 중단

  # 학생 정보를 딕셔너리로 만들어 리스트에 추가
  student_data = {'name': name, 'grade': grade, 'scores': {}} # 성적 저장 공간 추가
  students_db.append(student_data)
  print(f"[등록 완료] {name} 학생 정보가 추가되었습니다.")
  print(f"현재 학생 수: {len(students_db)}명")

def assign_score(student_name, subject, score):
  """특정 학생에게 과목 점수를 부여하는 절차"""
  global students_db
  print(f"\n[절차 시작] 성적 부여: 학생={student_name}, 과목={subject}, 점수={score}")

  student_found = False
  # 학생 데이터베이스(리스트)를 순차적으로 검색
  for student in students_db:
    if student['name'] == student_name:
      student['scores'][subject] = score # 해당 학생의 scores 딕셔너리에 점수 추가/수정
      print(f"[성적 입력 완료] {student_name} 학생의 {subject} 과목 점수가 {score}점으로 입력되었습니다.")
      student_found = True
      break # 학생을 찾았으므로 더 이상 검색할 필요 없음

  if not student_found:
    print(f"[오류] {student_name} 학생을 찾을 수 없습니다.")

def print_student_list():
  """전체 학생 명단과 정보를 출력하는 절차"""
  global students_db
  print("\n[절차 시작] 전체 학생 정보 출력")
  print("=" * 30)
  print("       < 전체 학생 현황 >")
  print("=" * 30)

  if not students_db:
    print("등록된 학생이 없습니다.")
    print("=" * 30)
    return # 절차 종료

  for student in students_db:
    print(f" 이름: {student['name']} ({student['grade']}학년)")
    if student['scores']:
      print("  * 성적:")
      for subject, score in student['scores'].items():
        print(f"    - {subject}: {score}점")
    else:
      print("  * 등록된 성적이 없습니다.")
    print("-" * 20) # 학생 간 구분선

  print("=" * 30)
  print("[출력 완료]")


# --- 프로그램 실행 흐름 (Main) ---

print("=== 학교 관리 프로그램 시작 (절차지향 방식) ===")

# 1. 학생 등록 절차 실행
register_student("김일남", 1)
register_student("김이남", 2)
register_student("김삼남", 1)
register_student("김일남", 3) # 중복 등록 시도

# 2. 성적 부여 절차 실행
assign_score("김일남", "수학", 85)
assign_score("김이남", "국어", 92)
assign_score("김일남", "과학", 90)
assign_score("김없음", "영어", 78) # 없는 학생에게 성적 부여 시도

# 3. 전체 학생 정보 출력 절차 실행
print_student_list()

print("\n=== 학교 관리 프로그램 종료 ===")
# 객체지향(Object Oriented Programming)
# --- 클래스 정의 (객체의 설계도) ---
class Student:
    """학생 한 명의 정보(속성)와 관련 기능(메서드)을 가지는 클래스"""
    def __init__(self, name, grade):
        # 객체가 생성될 때 호출되는 초기화 메서드 (생성자)
        self.name = name        # 학생 이름 속성
        self.grade = grade      # 학생 학년 속성
        self._scores = {}       # 성적 정보 (딕셔너리). _는 내부적으로 사용함을 암시 (캡슐화)
        print(f"  [Student 객체 생성] {self.grade}학년 {self.name} 학생 데이터 준비 완료.")

    def add_score(self, subject, score):
        """학생 자신의 성적을 추가/수정하는 메서드"""
        self._scores[subject] = score
        print(f"    >> {self.name} 학생에게 {subject} 과목 {score}점 입력 완료.")

    def get_info(self):
        """학생 자신의 정보를 문자열 형태로 반환하는 메서드"""
        info = f" 이름: {self.name} ({self.grade}학년)\n"
        if self._scores:
            info += "  * 성적:\n"
            # 자신의 _scores 속성을 사용하여 성적 정보 구성
            for subject, score in self._scores.items():
                info += f"    - {subject}: {score}점\n"
        else:
            info += "  * 등록된 성적이 없습니다.\n"
        return info

class School:
    """학교 운영(학생 관리, 성적 부여 등)을 담당하는 클래스"""
    def __init__(self, school_name):
        # 객체가 생성될 때 호출되는 초기화 메서드
        self.school_name = school_name # 학교 이름 속성
        self._students = []           # 학생 객체들을 저장할 리스트 (내부 관리)
        print(f"\n=== {self.school_name} 관리 시스템 시작 (객체지향 방식) ===")

    # 변수나 메서드 이름 앞에 밑줄(_)을 한 개 붙이면, "이 멤버는 내부적으로 사용하기 위한 것이거나, 상속받은 클래스에서 사용할 수 있지만, 클래스 외부에서 직접 사용하는 것은 권장하지 않는다"는 의미를 내포
    def _find_student(self, student_name):
        """이름으로 학생 객체를 찾는 내부 헬퍼 메서드"""
        for student_obj in self._students:
            # student_obj는 Student 클래스의 인스턴스(객체)
            if student_obj.name == student_name:
                return student_obj # 찾은 Student 객체를 반환
        return None # 못 찾으면 None 반환

    def register_student(self, name, grade):
        """학생을 학교 시스템에 등록하는 메서드"""
        print(f"\n[학교 기능] 학생 등록 시도: 이름={name}, 학년={grade}")
        # 이름 중복 체크 (내부 메서드 활용)
        if self._find_student(name):
             print(f"[오류] 이미 등록된 학생입니다: {name}")
             return

        # 1. Student 클래스를 이용해 학생 객체(인스턴스)를 생성
        new_student = Student(name, grade)
        # 2. 생성된 학생 객체를 학교의 학생 목록(_students 리스트)에 추가
        self._students.append(new_student)
        print(f"[등록 완료] {name} 학생이 {self.school_name}에 등록되었습니다.")
        print(f"현재 학생 수: {len(self._students)}명")

    def assign_score(self, student_name, subject, score):
        """특정 학생을 찾아 성적 입력을 지시하는 메서드"""
        print(f"\n[학교 기능] 성적 부여 시도: 학생={student_name}, 과목={subject}, 점수={score}")
        # 1. 이름으로 학생 객체 찾기
        student_object = self._find_student(student_name)

        # 2. 학생 객체를 찾았다면
        if student_object:
            # 3. 해당 학생 객체(student_object)에게 성적 추가를 요청 (메서드 호출)
            #    실제 성적 추가 로직은 Student 객체 내부에 있음 (책임 위임)
            student_object.add_score(subject, score)
        else:
            print(f"[오류] {student_name} 학생을 찾을 수 없습니다.")

    def print_school_report(self):
        """학교 전체 학생의 정보를 출력하는 메서드"""
        print("\n[학교 기능] 전체 학생 정보 출력")
        print("=" * 40)
        print(f"       < {self.school_name} 전체 학생 현황 >")
        print("=" * 40)

        if not self._students:
            print("등록된 학생이 없습니다.")
            print("=" * 40)
            return

        # 학교에 등록된 모든 학생 객체들을 순회
        for student_obj in self._students:
            # 각 학생 객체에게 자신의 정보를 달라고 요청 (get_info 메서드 호출)
            # 출력 형식 등은 Student 객체가 책임짐
            print(student_obj.get_info(), end='')
            print("-" * 20) # 학생 간 구분선

        print("=" * 40)
        print("[출력 완료]")

    def __del__(self):
        # 객체가 소멸될 때 호출되는 메서드 (선택적)
        print(f"\n=== {self.school_name} 관리 시스템 종료 ===")


# --- 프로그램 실행 흐름 (Main) ---

# 1. School 클래스를 이용해 '코리아IT아카데미'라는 School 객체(인스턴스) 생성
my_school = School("코리아IT아카데미")

# 2. 생성된 my_school 객체의 메서드를 호출하여 기능 실행
my_school.register_student("김일남", 1) # my_school 객체에게 김일남 학생 등록을 요청
my_school.register_student("김이남", 2)
my_school.register_student("김삼남", 1)
my_school.register_student("김일남", 3) # 중복 등록 시도 (School 객체가 처리)

# 3. my_school 객체에게 성적 부여를 요청
my_school.assign_score("김일남", "수학", 85)  # 내부적으로 김일남 Student 객체의 add_score 호출
my_school.assign_score("김이남", "국어", 92)
my_school.assign_score("김일남", "과학", 90)
my_school.assign_score("김없음", "영어", 78) # 없는 학생 처리 (School 객체가 처리)

# 4. my_school 객체에게 전체 학생 정보 출력을 요청
my_school.print_school_report()             # 내부적으로 각 Student 객체의 get_info 호출

# 프로그램이 끝나면 my_school 객체가 소멸되면서 __del__ 메서드가 (있다면) 호출됨
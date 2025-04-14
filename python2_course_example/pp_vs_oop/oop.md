네, 앞서 작성한 절차지향 코드를 객체지향 방식으로 변경한 파이썬 코드 예시입니다.

핵심은 **학생(`Student`)**과 **학교(`School`)**라는 **독립적인 역할과 책임(데이터와 기능)을 가진 객체**를 만들고, 이 **객체들이 서로 상호작용**하여 프로그램을 실행하는 것입니다.

```python
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

# 1. School 클래스를 이용해 '행복중학교'라는 School 객체(인스턴스) 생성
my_school = School("행복중학교")

# 2. 생성된 my_school 객체의 메서드를 호출하여 기능 실행
my_school.register_student("김민준", 1) # my_school 객체에게 김민준 학생 등록을 요청
my_school.register_student("이서연", 2)
my_school.register_student("박하늘", 1)
my_school.register_student("김민준", 3) # 중복 등록 시도 (School 객체가 처리)

# 3. my_school 객체에게 성적 부여를 요청
my_school.assign_score("김민준", "수학", 85)  # 내부적으로 김민준 Student 객체의 add_score 호출
my_school.assign_score("이서연", "국어", 92)
my_school.assign_score("김민준", "과학", 90)
my_school.assign_score("최지우", "영어", 78) # 없는 학생 처리 (School 객체가 처리)

# 4. my_school 객체에게 전체 학생 정보 출력을 요청
my_school.print_school_report()             # 내부적으로 각 Student 객체의 get_info 호출

# 프로그램이 끝나면 my_school 객체가 소멸되면서 __del__ 메서드가 (있다면) 호출됨

```

**절차지향 코드와의 주요 차이점:**

1.  **클래스와 객체**: 데이터(이름, 학년, 성적)와 그 데이터를 처리하는 기능(성적 추가, 정보 반환)이 `Student`라는 클래스 안에 **하나로 묶여(캡슐화)** 있습니다. `School` 클래스는 학생 객체들을 관리하고 학교 운영 관련 기능을 담당합니다.
2.  **책임 분담**: 성적을 추가하는 구체적인 방법은 `Student` 객체 자신이 알고 있습니다 (`add_score` 메서드). `School` 객체는 단지 특정 `Student` 객체를 찾아 "성적을 추가하라"고 **메시지를 보낼 뿐**(메서드 호출)입니다. 정보 출력도 마찬가지입니다 (`get_info`).
3.  **데이터 관리**: 학생 데이터는 더 이상 전역 리스트(`students_db`)가 아니라, `School` 객체 내부의 `_students` 리스트에 `Student` 객체 형태로 저장되고 관리됩니다. 외부에서 직접 접근하기보다 `School` 객체의 메서드를 통해 상호작용하는 것이 권장됩니다.
4.  **코드 구조**: 관련 데이터와 기능이 클래스 단위로 묶여있어, 코드를 이해하고 수정하기가 더 용이해집니다. 예를 들어 학생의 정보 형식을 바꾸려면 `Student` 클래스만 주로 수정하면 됩니다.

객체지향 방식은 이렇게 역할과 책임을 분리하고 객체 간의 협력을 통해 프로그램을 구성하므로, 더 크고 복잡한 프로그램을 만들 때 유지보수와 확장에 유리합니다.

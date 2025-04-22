# --- 클래스 정의 ---

class Student:
    """학생 한 명의 정보(속성)와 관련 기능(메서드)을 가지는 클래스"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self._scores = {}
        print(f"  [Student 객체 생성] {self.grade}학년 {self.name} 학생 데이터 준비 완료.")

    def add_score(self, subject, score):
        """학생 자신의 성적을 추가/수정하는 메서드"""
        self._scores[subject] = score
        print(f"    >> {self.name} 학생: {subject} 과목 점수 {score}점 입력됨.")

    # === 기능 추가: 평균 점수 계산 (캡슐화) ===
    def calculate_average_score(self):
        """학생 자신의 평균 점수를 계산하여 반환하는 메서드"""
        if not self._scores:
            return 0.0
        return sum(self._scores.values()) / len(self._scores)

    def get_info(self):
        """학생 자신의 정보를 문자열 형태로 반환하는 메서드 (평균 점수 기능 활용)"""
        avg_score = self.calculate_average_score() # 자신의 평균 계산 메서드 호출
        info = f" 이름: {self.name} ({self.grade}학년) [타입: 일반학생]\n" # 기본 타입 명시
        if self._scores:
            info += "  * 성적:\n"
            for subject, score in self._scores.items():
                info += f"    - {subject}: {score}점\n"
            info += f"  * 평균 점수: {avg_score:.2f}점\n" # 평균 점수 출력 추가
        else:
            info += "  * 등록된 성적이 없습니다.\n"
        return info

# === 새로운 클래스 추가 (상속 활용) ===
class GraduateStudent(Student): # Student 클래스를 상속받음!
    """대학원생을 나타내는 클래스 (Student 클래스를 확장)"""
    def __init__(self, name, grade, thesis_topic):
        # 1. 부모 클래스(Student)의 __init__을 호출하여 name, grade, _scores 초기화 (코드 재사용)
        super().__init__(name, grade)
        # 2. GraduateStudent만의 속성 추가
        self.thesis_topic = thesis_topic
        print(f"  [GraduateStudent 객체 생성] {self.name} 학생 (논문주제: {self.thesis_topic})")

    # === 메서드 오버라이딩 (Method Overriding) ===
    def get_info(self):
        """대학원생에 맞게 정보를 재정의(Override)하여 반환하는 메서드"""
        # 1. 부모 클래스(Student)의 get_info()를 호출하여 기본적인 정보(이름, 학년, 성적, 평균) 가져오기 (코드 재사용)
        basic_info = super().get_info()
        # 2. 부모 정보에서 타입 부분을 수정하고, 대학원생 고유 정보(논문 주제) 추가
        info_with_type_change = basic_info.replace("[타입: 일반학생]", "[타입: 대학원생]") # 타입 문자열 변경
        info_with_topic = info_with_type_change + f"  * 논문 주제: {self.thesis_topic}\n" # 논문 정보 추가
        return info_with_topic

    # add_score, calculate_average_score 메서드는 Student로부터 상속받았으므로 재정의할 필요 없음 (코드 재사용)


class School:
    """학교 운영을 담당하는 클래스"""
    def __init__(self, school_name):
        self.school_name = school_name
        # === _students 리스트에는 Student 객체와 GraduateStudent 객체 모두 저장 가능! ===
        self._students = []
        print(f"\n=== {self.school_name} 관리 시스템 시작 (객체지향 방식) ===")

    def _find_student(self, student_name):
        """이름으로 학생 객체(Student 또는 GraduateStudent)를 찾는 내부 메서드"""
        for student_obj in self._students:
            if student_obj.name == student_name:
                return student_obj
        return None

    # 학생 등록 메서드를 분리하여 명확성 높임
    def register_student(self, name, grade):
        """일반 학생을 학교 시스템에 등록"""
        print(f"\n[학교 기능] 일반 학생 등록 시도: 이름={name}, 학년={grade}")
        if self._find_student(name):
             print(f"[오류] 이미 등록된 학생입니다: {name}")
             return
        new_student = Student(name, grade) # Student 객체 생성
        self._students.append(new_student) # 리스트에 추가
        print(f"[등록 완료] {name} 일반 학생이 {self.school_name}에 등록되었습니다.")
        print(f"현재 학생 수: {len(self._students)}명")

    def register_graduate_student(self, name, grade, thesis_topic):
        """대학원생을 학교 시스템에 등록"""
        print(f"\n[학교 기능] 대학원생 등록 시도: 이름={name}, 학년={grade}, 주제={thesis_topic}")
        if self._find_student(name):
             print(f"[오류] 이미 등록된 학생입니다: {name}")
             return
        # GraduateStudent 객체 생성
        new_grad_student = GraduateStudent(name, grade, thesis_topic)
        # === 동일한 _students 리스트에 추가! School 클래스는 구체적인 타입을 몰라도 됨 ===
        self._students.append(new_grad_student)
        print(f"[등록 완료] {name} 대학원생이 {self.school_name}에 등록되었습니다.")
        print(f"현재 학생 수: {len(self._students)}명")


    def assign_score(self, student_name, subject, score):
        """학생 이름으로 찾아 성적 부여 (학생 타입 무관)"""
        # === 이 메서드는 학생 타입이 추가되어도 수정할 필요가 없음! ===
        # _find_student가 어떤 타입의 학생 객체든 찾아주고,
        # 모든 학생 객체는 add_score 메서드를 가지고 있기 때문 (상속 덕분)
        print(f"\n[학교 기능] 성적 부여 시도: 학생={student_name}, 과목={subject}, 점수={score}")
        student_object = self._find_student(student_name)
        if student_object:
            # student_object가 Student든 GraduateStudent든 상관없이 add_score 호출
            student_object.add_score(subject, score)
        else:
            print(f"[오류] {student_name} 학생을 찾을 수 없습니다.")

    def print_school_report(self):
        """학교 전체 학생 정보 출력 (학생 타입 무관)"""
        # === 이 메서드도 학생 타입이 추가되어도 수정할 필요가 없음! (다형성의 장점) ===
        print("\n[학교 기능] 전체 학생 정보 출력")
        print("=" * 50) # 구분선 길이 조정
        print(f"       < {self.school_name} 전체 학생 현황 >")
        print("=" * 50)

        if not self._students:
            print("등록된 학생이 없습니다.")
            print("=" * 50)
            return

        # _students 리스트에는 Student와 GraduateStudent 객체가 섞여있음
        for student_obj in self._students:
            # student_obj 변수에는 Student 객체 또는 GraduateStudent 객체가 번갈아 담김
            # 하지만 어떤 객체든 get_info() 메서드를 가지고 있음
            # 파이썬은 객체의 실제 타입에 맞는 get_info()를 알아서 호출해줌 (다형성)
            print(student_obj.get_info(), end='') # 각 객체가 자신의 정보 형식에 맞게 출력
            print("-" * 30) # 학생 간 구분선 조정

        print("=" * 50)
        print("[출력 완료]")

    def __del__(self):
         print(f"\n=== {self.school_name} 관리 시스템 종료 ===")


# --- 프로그램 실행 흐름 (Main) ---

my_university = School("융합대학교") # 학교 이름 변경

# 일반 학생 등록
my_university.register_student("김민준", 1)
my_university.register_student("이서연", 2)

# === 대학원생 등록 (새로운 유형 추가) ===
my_university.register_graduate_student("박지성", 5, "머신러닝 기반 자연어 처리") # 대학원생 등록

# 성적 부여 (Student, GraduateStudent 구분 없이 이름으로 부여)
my_university.assign_score("김민준", "파이썬 기초", 90)
my_university.assign_score("이서연", "객체지향 설계", 85)
my_university.assign_score("박지성", "딥러닝 연구", 95) # 대학원생에게 성적 부여
my_university.assign_score("김민준", "웹 프로그래밍", 88)
my_university.assign_score("박지성", "컴퓨터 비전 세미나", 100)

# 전체 학생 정보 출력
# === School 클래스의 print_school_report는 수정 없이도 알아서 처리 ===
my_university.print_school_report()
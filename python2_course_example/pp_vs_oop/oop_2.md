네, 객체지향 프로그래밍(OOP)의 장점을 더 명확하게 보여주기 위해 기존 학교 프로그램 코드를 수정해 보겠습니다. 특히 **유지보수 용이성, 확장성, 코드 재사용성** 측면을 강조할 수 있도록 변경해 봅시다.

**수정 방향:**

1.  **기능 추가 (캡슐화 및 응집도):** 학생 객체(`Student`) 스스로 자신의 평균 점수를 계산하는 기능을 추가합니다. 관련 데이터와 기능이 한곳에 모여있음을 보여줍니다.
2.  **새로운 유형 추가 (상속 및 확장성):** '일반 학생' 외에 '대학원생'이라는 새로운 유형의 학생을 추가합니다. 대학원생은 일반 학생의 특징을 공유하면서(이름, 학년, 성적 등) 추가 정보(논문 주제)를 가집니다. 이는 **상속(Inheritance)**을 통해 코드 재사용성을 높이고 시스템을 쉽게 **확장**하는 예시가 됩니다.
3.  **동일 인터페이스, 다른 동작 (다형성):** 학교 시스템(`School`)은 학생의 실제 유형(일반학생인지 대학원생인지)에 크게 신경 쓰지 않고 동일한 방식(`get_info()`)으로 정보를 요청하지만, 각 객체는 자신의 유형에 맞게 다른 정보를 반환합니다. 이는 **다형성(Polymorphism)**의 장점을 보여줍니다.

**수정된 코드:**

```python
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

```

**수정된 코드에서 확인 가능한 객체지향의 장점:**

1.  **캡슐화 (Encapsulation) 및 응집도 (Cohesion):**

    - 학생의 평균 점수 계산 로직(`calculate_average_score`)이 `Student` 클래스 내부에 포함되었습니다. 성적 데이터(`_scores`)와 이를 처리하는 로직이 한곳에 모여있어 **응집도**가 높습니다.
    - 만약 평균 계산 방식을 변경해야 한다면(예: 특정 과목 가중치 부여), `Student` 클래스 내부만 수정하면 됩니다. 외부 코드(예: `School` 클래스)는 영향을 받지 않습니다. 이것이 **캡슐화**의 장점입니다.

2.  **상속 (Inheritance) 및 코드 재사용 (Reusability):**

    - `GraduateStudent` 클래스는 `Student` 클래스를 **상속**받아 `name`, `grade`, `_scores` 속성과 `add_score`, `calculate_average_score` 메서드를 그대로 **물려받아 재사용**합니다. 동일한 코드를 다시 작성할 필요가 없어 효율적입니다.
    - `GraduateStudent`는 필요한 `thesis_topic` 속성과 `get_info` 메서드 오버라이딩만 추가/수정했습니다.

3.  **다형성 (Polymorphism) 및 유연성 (Flexibility):**

    - `School` 클래스의 `assign_score`와 `print_school_report` 메서드는 학생 객체의 실제 타입이 `Student`인지 `GraduateStudent`인지 **구분하지 않고 동일한 방식**으로 상호작용합니다.
    - `_students` 리스트에 어떤 타입의 학생 객체가 들어있든, `student_obj.add_score()`나 `student_obj.get_info()`를 호출하면 파이썬이 **자동으로 해당 객체 타입에 맞는 메서드를 실행**해 줍니다.
    - 이 덕분에 `School` 클래스는 새로운 종류의 학생(예: `ExchangeStudent`)이 추가되더라도, 그 학생 클래스가 `add_score`, `get_info` 와 같은 **약속된 인터페이스(메서드)**만 제공한다면 **`School` 클래스 코드를 거의 수정하지 않고도** 새로운 학생 유형을 처리할 수 있습니다. 이것이 다형성이 제공하는 **유연성**입니다.

4.  **확장성 (Extensibility) 및 유지보수성 (Maintainability):**
    - '대학원생'이라는 새로운 요구사항이 생겼을 때, 기존 `Student`나 `School` 코드를 크게 변경하는 대신, `Student`를 상속받는 `GraduateStudent` 클래스를 **새로 추가**하고 `School`에 등록 메서드(`register_graduate_student`) 정도만 추가하여 시스템을 **쉽게 확장**했습니다.
    - 각 클래스가 자신의 책임(학생 정보 관리, 학교 운영 관리)에 집중하므로 코드를 이해하고 수정하기가 더 쉬워져 **유지보수성**이 향상됩니다.

이처럼 객체지향 프로그래밍은 관련 데이터와 기능을 묶어 관리하고(캡슐화), 코드 재사용성을 높이며(상속), 유연하고 확장 가능한 시스템(다형성, 확장성)을 만드는 데 도움을 줍니다. 특히 프로그램의 규모가 커지고 요구사항 변경이 잦을수록 이러한 장점들이 더욱 중요해집니다.

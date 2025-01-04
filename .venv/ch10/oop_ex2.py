'''
파일명: oop_ex2.py
위치: .venv/ch10/
'''


# 인스턴스의 클래스 확인하기

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print("공부를 합니다.")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print("강의를 합니다.")

# 객체 생성
student1 = Student("학생1")
student2 = Student("학생1")
teacher1 = Teacher("강사1", "컴퓨터")

class_a = [student1, teacher1, student2]

for member in class_a:
    print(member.name)

    if isinstance(member, Teacher):
        # 현재 member(인스턴스)가 Teacher 클래스의 객체이면 subject 필드 출력 + teach() 메소드 호출
        print(member.subject)
        member.teach()
    elif isinstance(member, Student):
        # 현재 member(인스턴스)가 Student 클래스의 객체이면 study() 메소드 호출
        member.study()

'''
파일명: oop_ex3.py
위치: .venv/ch10/
'''


# 클래스 변수
class Student:
    # 클래스 변수 선언
    student_count = 0

    def __init__(self, name):
        # 각 각의 인스턴스마다 따로 존재하는 데이터
        self.name = name;

        # 학생 전체수 1증가
        Student.student_count += 1

    @classmethod # 데코레이터
    def intro_school(cls):
        print(f"우리 학교의 재원생은 {cls.student_count}명입니다.")


student1 = Student("영철")
print(student1.name, student1.student_count)

student2 = Student("옥순")
print(student2.name, student2.student_count)

student3 = Student("영철")
print(student3.name, student3.student_count)

Student.intro_school()


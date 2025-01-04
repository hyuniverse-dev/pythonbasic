'''
파일명: extend_practice1.py
위치: .venv/ch10/
'''
from time import sleep


# Person 클래스 정의
#   속성: name, age, gender
#   기능: introduce()
#         "안녕하세요. 제 이름은 000입니다. 저는 00살입니다."
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}입니다. 저는 {self.age}살입니다.")


# Student 클래스 정의 - Person 상속
#   추가 속성: korean, math, english
class Student(Person):
    def __init__(self, name, age, gender, korean, math, english):
        super().__init__(name, age, gender)
        self.korean = korean
        self.math = math
        self.english = english


# Teacher 클래스 정의 - Person 상속
#   추가 속성: subject
class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject


############################################

# Student 인스턴스 생성 후 name, age, gender, korean, math, english 점수 출력
student = Student("박현", 20, "남성", 80, 90, 95)
print(student.name, student.age, student.gender, student.korean, student.math, student.english)
student.introduce()

# Teacher 인스턴스 생성 후 name, age, gender, subject 출력
teacher = Teacher("박현", 20, "남성", "파이썬")
print(teacher.name, teacher.age, teacher.gender, teacher.subject)
teacher.introduce()
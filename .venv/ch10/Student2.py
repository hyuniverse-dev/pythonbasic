'''
파일명: Student2.py
위치: .venv/ch10/
'''


# 설계도
#   학생: 이름, 학년, 성별, 학교명
class Student2:
    def __init__(self, name, grade, gender, schoolname):
        print("생성자 함수 호출!")
        self.name = name
        self.grade = grade
        self.schoolname = schoolname
        self.gender = gender


# 객체 생성(Student2 설계도 사용)
student = Student2("박현", "1학년", "남자", "신촌대학교")
print(student.name, student.grade, student.grade, student.schoolname)


# 속성: 브랜드(brand), 색상(color), 연료(종류)(fuel)
class Car:
    # 생성자 함수
    def __init__(self, brand, color, fuel, price):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        # 가격(price) = 부가세 10% 포함된 가격으로 데이터 저장
        self.price = int(price * 1.1)


# Car 객체 생성
#   1. 현대, 블랙, 휘발유
car1 = Car("현대", "블랙", "휘발유", 2000000)
print(car1.brand, car1.color, car1.fuel, car1.price)

#   2. 기아, 화이트, 경유
car2 = Car("기아", "화이트", "경유", 1780000)
print(car2.brand, car2.color, car2.fuel, car2.price)


# Student3 클래스 정의
#   - 속성: 이름, 국어 점수, 수학 점수, 영어 점수
#   - 기능: 총점을 반환하는 메소드 구현
class Student3:
    # 생성자
    def __init__(self, name, korean, math, english, computer):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.computer = computer

    def get_sum(self):
        return self.korean + self.math + self.english + self.computer

    # 평균 구하는 기능 추가(get_average)
    def get_average(self):
        return self.get_sum() / 4


# 객체 생성
student = Student3("박현", 90, 80, 99, 100)
total = student.get_sum()
print(total)

# student 의 평균 출력
average = student.get_average()
print(average)

'''
파일명: oop_ex1.py
위치: .venv/ch10/
'''


# 객체지향 프로그래밍으로 넘어가기
#   - 학생 관리 프로그램

# 학생 데이터 생성하는 함수
def create_student(name, korean, english, math, gender):
    return {
        "name": name,
        "korean": korean,
        "english": english,
        "math": math,
        "gender": gender
    }


# 학생 데이터 버전(1)
# students = [
#     {"name": "옥순", "korean": 87, "english": 98, "math": 90},
#     {"name": "영자", "korean": 17, "english": 89, "math": 90},
#     {"name": "영철", "korean": 47, "english": 80, "math": 90},
#     {"name": "영수", "korean": 82, "english": 85, "math": 90}
# ]

# 학생 데이터 버전(2)
students = [
    create_student("옥순", 87, 98, 90),
    create_student("영자", 17, 80, 34),
    create_student("영철", 47, 11, 16),
    create_student("영수", 90, 80, 99),
    create_student("정숙", 90, 99, 100)
]

# 학생의 기능(1): 자기소개 기능
def sayHello(name):
    print(f"안녕하세요 저는 {name}입니다!")


# 학생의 기능(2): 총점과 평균을 구하는 기능
print("이름", "총점", "평균", sep='\t')
for student in students:
    # 총점과 평균 구하기
    total = student['korean'] + student['english'] + student['math']
    average = total / 3
    sayHello(student['name'])
    print(f"{student['name']}", total, average, sep='\t')

# 예시: 새로운 학생을 생성해서 자기소개 시키기
student = create_student("철수", 100, 90, 80)
sayHello(student['name'])
sayHello("Hello Python")







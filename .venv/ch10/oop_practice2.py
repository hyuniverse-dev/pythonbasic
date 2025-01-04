'''
파일명: oop_practice2.py
위치: .venv/ch10/
'''


# 클래스 변수와 클래스 메소드 정의하기
class Teacher:
    # 1. 전체 선생님의 수를 누적하는 클래스 변수 선언
    teacher_count = 0

    # 2. "A대학교" 문자열 데이터를 가지고 있는 클래스 변수 선언
    school_name = "A대학교"

    # 3. 속성: name, subject
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

        # 객체 생성 시에 카운트 1증가
        Teacher.teacher_count += 1

    # 4. "A대학교 전체 선생님의 수: 10명" 출력이 되도록
    #    클래스 메소드를 정의
    @classmethod
    def intro_school(cls):
        print(f"{cls.school_name} 전체 선생님의 수: {cls.teacher_count}명")
    

# 객체 생성 - Teacher 객체 3개 생성 + intro_school 클래스 메소드 호출
teacher1 = Teacher("영철", "컴퓨터")
print(Teacher.teacher_count)

teacher2 = Teacher("영자", "음악")
print(Teacher.teacher_count)

teacher3 = Teacher("정숙", "가정")
print(Teacher.teacher_count)

Teacher.intro_school()









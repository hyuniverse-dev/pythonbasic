'''
파일명: list_ex1.py
위치: .venv/ch05/
'''

# 리스트
#   - 여러가지 데이터를 저장할 수 있는 자료입니다.
#   - 순서가 존재합니다.
#   - 중복을 허용합니다.
#   - 반복이 가능한 객체입니다.

# 학생 이름 저장하기 - 리스트 미사용
student_name1 = "옥순"
student_name2 = "영수"
student_name3 = "정숙"
print(student_name1, student_name2, student_name3, sep=', ')

# 학생 이름 저장하기 - 리스트 사용
students = ["옥순", "영수", "정숙"]
print(students)

# 빈리스트
numbers = []
print(numbers)

# 1. 리스트 생성하기
#   - 대괄호에 자료를 쉼표로 구분해서 입력합니다.
#   - 내부에 넣는 자료를 요소(Elements)라고 합니다.
#   - 순서가 존재합니다.
#   - 여러 종류의 자료형으로 구성할 수 있습니다.
numbers = [1, 2, 3, 4]
strings = ["Python", "Java", "C"]
mixed = [123, "Hello World", 3.14]

print(numbers)
print(strings)
print(mixed)

# 2. 리스트의 요소에 접근하기
#   - 리스트명 뒤에 대괄호를 입력(기술)하고, 요소의 위치를 나타내는 정수를 사용합니다.
hello = ["안", "녕", "하", "세", "요"]
print(hello[0])
print(hello[2])
print(hello[-1])
print(hello[-2])

# 3. 리스트의 여러 요소에 접근하기 - 슬라이싱
#   - 특정 범위의 여러 데이터를 슬라이싱하여 접근합니다.
#   - 선택하는 요소의 끝 인덱스는 +1 한 값으로 작성합니다.
print(hello[:2])
print(hello[3:]) # 슬라이싱으로 동일한 결과를 출력하세요.

# 4. 리스트 요소에 접근시 주의할 점
#   - 인덱스로 요소에 접근할 때 존재하지 않는 인덱스를 사용하면 에러 발생합니다.
#   - IndexError 가 발생합니다.
# print(hello[5])

# 5. 리스트 요소를 수정하기
#   - 수정할 요소에 인덱스로 접근하고 새로운 데이터 대입
hello[4] = "용"
print(hello)
hello[3:] = ["신", "가"]
print(hello)






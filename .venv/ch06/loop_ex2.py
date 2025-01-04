'''
파일명: loop_ex2.py
위치: .venv/ch06/
'''

# 실습 문제

# 1번. 리스트 요소 중 100 이상의 숫자만 출력하도록 프로그램 완성하세요.
numbers = [273, 103, 6, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print(number)

# 2번. 리스트 요소의 홀/짝을 판별하는 프로그램을 완성하세요.
#   - 출력 형식: 6는 짝수입니다. / 99는 홀수입니다.
numbers = [273, 103, 6, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number % 2 == 0:
        print(f"{number}은/는 짝수입니다.")
    else:
        print(f"{number}은/는 홀수입니다.")

# 3번. 다음과 같은 형식으로 리스트 요소의 각 자릿수를 출력하는 프로그램을 완성하세요.
'''
✅ <실행 결과>

273 는 3 자릿수입니다.
103 는 3 자릿수입니다.
5 는 1 자릿수입니다.
32 는 2 자릿수입니다.
65 는 2 자릿수입니다.
9 는 1 자릿수입니다.
72 는 2 자릿수입니다.
800 는 3 자릿수입니다.
99 는 2 자릿수입니다.
'''
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    print(f"{number} 는 {len(str(number))} 자릿수입니다.")

# 4번. 다음 빈칸을 채워서 사용자로부터 입력받아 "Todo List" 를 다음과 같이 출력하는 프로그램을 완성하세요.
'''
✅ <실행 결과>
할 일 목록(1): 운동하기
할 일 목록(2): 파이썬 복습하기
할 일 목록(3): 샤워하기
할 일 목록(4): 독서하기
'''

todo_list = []  # 할 일 목록을 저장할 빈 리스트 생성
user_input = ""  # 사용자 입력을 저장할 빈 문자열 생성
while user_input.lower() != 'quit':  # 사용자가 'quit'을 입력할 때까지 반복
    user_input = input("Todo List를 입력하세요.(종료하려면 'quit') >>> ")
    if user_input.lower() != 'quit':  # 사용자가 'quit'을 입력한 경우에는 리스트에 추가하지 않음
        todo_list.append(user_input)  # 사용자 입력을 리스트에 추가

count = 1
for todo in todo_list:
    print(f"할 일 목록({count}): {todo}")
    count += 1







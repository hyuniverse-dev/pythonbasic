'''
파일명: function_ex2.py
위치: .venv/ch08/
'''


# 1. 전달받은 문자열을 n번 출력하는 함수
def print_n_times(value, times):
    # 반복문
    for i in range(times):
        print(value)


# 2. print_n_times 호출
#   - 정의된 함수의 매개변수보다 적게/많게 인수를 전달하면 에러가 발생합니다.
#   - 정의된 함수의 매개변수 순서에 맞도록 인수를 전달해야 합니다.
print_n_times("[4주차] 함수 단원 학습", 3)


# 3. 가변 매개변수 사용하기
#   - 여러 개의 문자열을 받아서 n번 출력하는 함수
def print_n_times2(n, *value):
    # 반복문
    for i in range(n):
        for item in value:
            print(item)

# 4. print_n_time2 호출
print_n_times2(3, "안녕하세요", "파이썬 수업", "4주차", "1교시", "가변 매개변수")

# 5. 기본 매개변수 사용하기
#   - 문자열을 받아서 n번 출력하는 함수. 기본은 한 번만 출력
def print_n_times3(value, times = 1):
    for i in range(times):
        print(value)

# 6. print_n_time3 호출
print_n_times3("Hello")
print_n_times3("Hello2", 5)













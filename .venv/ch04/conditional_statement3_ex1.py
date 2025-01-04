'''
파일명: conditional_statement3_ex1.py
위치: .venv/ch04/
'''

# 삼항연산자
#   세 개의 피연산자를 가지고 조건에 따라 값을 반환하는 연산자입니다.

a = 1
b = 7

message = "a가 b보다 큽니다." if a > b else "b가 a보다 큽니다."
print(message)

# 위 표현식을 기본 if문으로 변경
if a > b:
    message = "a가 b보다 큽니다."
else:
    message = "b가 a보다 큽니다."
print(message)


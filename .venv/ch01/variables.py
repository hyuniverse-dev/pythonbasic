'''
파일명: variables.py
위치: .venv/ch01
'''

# 변수는 변수명과 데이터(값)로 구성이 되어 있습니다.
#   데이터: 문자열("안녕하세요"), 숫자(10, 3.14, ..)

message = "안녕하세요."
age = 10
pi = 3.14
print(message) # 안녕하세요.

message = "Hello"
print(message) # Hello

# 변수를 사용하는 이유 - 데이터 재사용이 가능합니다.
x = 20
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# (1) a 라는 변수에 숫자 100 을 저장하세요.
a = 100

# (2) print() 함수를 사용해서 a 변수의 값을 console 에 출력하세요.
print(a)


# (3) a 변수의 값을 200 으로 새로 저장하세요.
a = 200

# (4) print() 함수를 사용해서 a 변수의 새로운 값을 console 에 출력하세요.
print(a)

# 파이썬 예약어 리스트
import keyword
print(keyword.kwlist) # 파이썬 예약어 리스트 출력
# continue = 10 -> 파이썬 예약어이기 때문에 변수명으로 사용불가






















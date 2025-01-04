'''
파일명: type_casting_ex1.py
위치: ./venv/ch03
'''

# 타입 캐스팅(Type Casting)

# 1. 타입 확인하기
#   - 자료형변환 하기 전에 현재 변수에 담겨있는 값의 자료형을 확인합니다.

number_value = 1
string_value = "String"
float_value = 1.0

print(type(number_value))
print(type(string_value))
print(type(float_value))

# 1-1. input() 함수의 반환값 타입 확인하기
# x = input("값을 입력하세요: ")
# print(type(x))

# 2. 정수형으로 형변환하기
#   - 입력받은 데이터를 정수로 사용할 수 있도록 자료형을 변환합니다.
#   - 정수형으로 형변환 가능한 데이터만 허용합니다.
value = int("10")
print(type(value))

value = int(False)
print(f"값: {value}, 타입: {type(value)}")

# 2-1. input_ex2.py 예제 해결하기
x = input("첫 번째 숫자를 입력하세요 >>> ")
y = input("두 번째 숫자를 입력하세요 >>> ")
print(int(x) + int(y))
print(int(x) - int(y))

# 2-2. 위 코드 리팩토링하기
x = int(input("첫 번째 숫자를 입력하세요2 >>> "))
y = int(input("두 번째 숫자를 입력하세요2 >>> "))
print(x + y)
print(x - y)
print(x * y)

# 3. 실수형으로 형변환하기
#   - 실수형으로 형변환 가능한 데이터만 허용합니다.
value = float("10.0")
print(type(value))

value = float(False)
print(f"값: {value}, 타입:{type(value)}")

# 4. 정수 또는 실수를 문자형으로 형변환하기
value = str(10)
print(type(value))
print(f"값:{value}, 타입:{type(value)}")

value = str(3.14)
print(f"값:{value}, 타입:{type(value)}")

value = str(True)
print(f"값:{value}, 타입:{type(value)}")

value = str(False)
print(f"값:{value}, 타입:{type(value)}")








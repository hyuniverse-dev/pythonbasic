'''
파일명: conditional_statement_ex4.py
위치: ./venv/ch04
'''

'''
조건문 실습3

(기획)
    사용자로부터 세 개의 숫자를 입력받고 가장 큰 수를 출력하기

(표준입력)
    1. 첫 번째 숫자를 입력해주세요. >>> 99
    2. 두 번째 숫자를 입력해주세요. >>> 15
    3. 세 번째 숫자를 입력해주세요, >>> 0
(표준출력)
    가장 큰 수는 99입니다.
'''

number1 = int(input("첫 번째 숫자를 입력해주세요 >>> "))
number2 = int(input("두 번째 숫자를 입력해주세요 >>> "))
number3 = int(input("세 번째 숫자를 입력해주세요 >>> "))

max = 0

# 가장 큰 수를 찾아오기
if number1 > number2 and number1 > number3:
    max = number1
elif number2 > number1 and number2 > number3:
    max = number2
else:
    max = number3

# 출력문은 한 줄로 정리
print(f"가장 큰 수는 {max}입니다.")

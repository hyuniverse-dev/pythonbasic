'''
파일명: conditional_statement_ex1.py
위치: ./venv/ch04
'''

# 조건문
#   - 주어진 조건이 참(True)인 경우에만 특정 코드 블록을 실행합니다.
#   - 실행할 코드는 indent(들여쓰기)로 구분합니다.

# 1. if문
number = -1

if number > 0:
    print("선택하신 숫자는 '양수' 입니다.")

print("##############################")

# 2. if-else문
number = 0

if number > 0:
    print("선택하신 숫자는 '양수' 입니다.")
else:
    print("선택하신 숫자는 '음수' 입니다.")

print("##############################")

# 3. if-elif-else문 (다중 조건 처리)
if number > 0:
    print("선택하신 숫자는 '양수' 입니다.")
elif number == 0:
    print("선택하신 숫자는 '0' 입니다.")
else:
    print("선택하신 숫자는 '음수' 입니다.")

print("##############################")

score = 65

if score >= 90:
    print("A등급 입니다.")
elif score >= 80:
    print("B등급 입니다.")
elif score >= 70:
    print("C등급 입니다.")
elif score >= 60:
    print("D등급 입니다.")
else:
    print("E등급 입니다.")






print("프로그램 종료")
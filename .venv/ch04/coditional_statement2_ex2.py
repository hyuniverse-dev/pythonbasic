'''
파일명: conditional_statement2_ex2.py
위치: .venv/ch04/
'''

# 1. 학생 점수 입력받기
name = input("학생의 이름을 입력하세요 >>> ")
korean = int(input("국어 >>> "))
english = int(input("영어 >>> "))
math = int(input("수학 >>> "))

is_valid = False

# 2. 유효한 점수인지 확인하기 - 유효성 체크
if not (0 <= korean <= 100):
    is_valid = True
    print(f"{name}: 국어 점수 입력 오류입니다.(입력값: {korean})")
elif not (0 <= english <= 100):
    is_valid = True
    print(f"{name}: 국어 점수 입력 오류입니다.(입력값: {english})")
elif not (0 <= math <= 100):
    is_valid = True
    print(f"{name}: 국어 점수 입력 오류입니다.(입력값: {math})")

if is_valid != True:
    # 3. 평균 점수 구하기
    total = korean + english + math
    average = total / 3

    # 4. 보충학습 대상인지 판별하기
    if average >= 80:
        print("보충학습 대상이 아닙니다.")
    else:
        # 4-1. 점수 구하기
        differ = 80 - average
        print(f"보충학습 대상입니다. (점수차: {round(differ, 2)}점)")

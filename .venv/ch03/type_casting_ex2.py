'''
파일명: type_casting_ex2.py
위치: ./venv/ch03
'''

'''
자료형 변환 실습

- 사용자로부터 태어난 연도를 입력받아 현재 나이를 출력해주세요.

- 표준입력
    태어난 연도를 입력하세요 >>> 

- 표준출력
    현재 나이는 XX세 입니다.
'''

year = int(input("태어난 연도를 입력하세요 >>> "))
print(f"값:{year}, 타입:{type(year)}")

age = 2024 - year

print(f"현재 나이는 {age}세 입니다.")







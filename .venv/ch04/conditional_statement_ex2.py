'''
파일명: condotional_statement_ex.py
위치: .venv/ch04/
'''

'''
조건문 실습 (1)

(기획)
    사용자로부터 비밀번호를 입력받아 정합성 판단하기

(조건)
    사용자가 입력한 비밀번호와 비교할 비밀번호는 "aaa123" 입니다.

(표준입력)
    비밀번호를 입력하세요 >>>

(표준출력)
    1. 비밀번호를 입력하지 않았을 때 -> 비밀번호를 입력해주세요.
    2. 비밀번호가 일치할 때 -> 비밀번호가 일치합니다!
    3. 비밀번호가 불일치 할 때 -> 비밀번호가 불일치합니다!
'''
origin_password = "aaa123"
input_password = input("비밀번호를 입력하세요 >>> ")

# 권장하는 코드
if input_password == origin_password:
    print("비밀번호가 일치합니다!")
elif input_password == "":
    print("비밀번호를 입력해주세요.")
else:
    print("비밀번호가 불일치합니다!")

print("#################################")

# 순서 주의해야 하는 경우
if input_password == "":
    print("비밀번호를 입력해주세요.")
elif input_password == origin_password:
    print("비밀번호가 일치합니다!")
else:
    print("비밀번호가 불일치합니다!")

print("#################################")

# 버그가 생기는 경우 (빈문자열 처리할 때 버그 발생)
if input_password != origin_password:
    print("비밀번호가 불일치합니다!")
elif input_password == "":
    print("비밀번호를 입력해주세요.")
else:
    print("비밀번호가 일치합니다!")

print("#################################")

if input_password == origin_password:
    print("비밀번호가 일치합니다!")
elif input_password != origin_password:
    print("비밀번호가 불일치합니다!")
else:
    print("비밀번호를 입력해주세요.")








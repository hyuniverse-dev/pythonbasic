'''
파일명: conditional_statement2_ex4.py
위치: .venv/ch04/
'''

# 문자열의 개수 세는 방법 (len() 함수는 공백도 포함합니다.)
string_len = len("파이썬")

# 문자열의 개수가 5 이상인지 판별하기
if string_len >= 5:
    print("현재 변수의 길이는 5 이상입니다.")
else:
    print("현재 변수의 길이는 5 미만입니다.")

'''
(기획)
    사용자로부터 아이디와 비밀번호를 입력받아 회원가입 처리하기

(조건)
    아이디와 비밀번호는 10자리 이하 이여야 합니다.

(표준입력)
    (테스트 케이스1)
    1. 사용하실 ID 를 입력해주세요. >>> tester1
    2. 사용하실 PASSWORD 를 입력해주세요. >>> tester1

    (테스트 케이스2)
    1. 사용하실 ID 를 입력해주세요. >>> tester12341234
    2. 사용하실 PASSWORD 를 입력해주세요. >>> tester1

    (테스트 케이스3)
    1. 사용하실 ID 를 입력해주세요. >>> tester1
    2. 사용하실 PASSWORD 를 입력해주세요. >>> tester12341234

(표준출력)
    (테스트 케이스1)
    회원가입에 성공하셨습니다.

    (테스트 케이스2)
    아이디가 10자리를 초과했습니다.

    (테스트 케이스3)
    비밀번호가 10자리를 초과했습니다.
'''

input_id = input("사용하실 ID를 입력해주세요 >>> ")
input_password = input("사용하실 PASSWORD를 입력해주세요 >>> ")

id_len = len(input_id)
password_len = len(input_password)

if len(input_id) <= 10:
    if len(input_password) <= 10:
        print("회원가입 성공하셨습니다!")
    else:
        print("비밀번호가 10자리를 초과했습니다.")
else:
    print("아이디가 10자리를 초과했습니다.")




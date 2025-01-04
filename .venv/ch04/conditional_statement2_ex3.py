'''
파일명: conditional_statement_ex3.py
위치: .venv/ch04/
'''

'''
조건문응용 실습

(기획)
    사용자로부터 입력받은 아이디와 비밀번호를 검증 후 로그인 처리하기

(조건)
    회원가입시 입력한 정보는 다음과 같고, 데이터의 타입 모두 String 입니다.
    1. 아이디 : tester
    2. 비밀번호 : 1234

(표준입력)
    (테스트 케이스1)
    1. 사용하실 ID 를 입력해주세요. >>> tester
    2. 사용하실 PASSWORD 를 입력해주세요. >>> 1234

    (테스트 케이스2)
    1. 사용하실 ID 를 입력해주세요. >>> testerrr
    2. 사용하실 PASSWORD 를 입력해주세요. >>> 1234

    (테스트 케이스3)
    1. 사용하실 ID 를 입력해주세요. >>> tester
    2. 사용하실 PASSWORD 를 입력해주세요. >>> 1111

(표준출력)
		(테스트 케이스1)
		로그인에 성공하셨습니다.

		(테스트 케이스2)
		아이디를 확인해주세요.

		(테스트 케이스3)
		비밀번호를 확인해주세요.
'''

origin_id = "tester"
origin_password = "1234"

input_id = input("사용하실 ID를 입력해주세요 >>> ")
input_password = input("사용하실 PASSWORD를 입력해주세요 >>> ")

# 1. 아이디 검사
if input_id == origin_id:
    # 2. 비밀번호 검사
    if input_password == origin_password:
        print("로그인에 성공하셨습니다.")
    else:
        print("비밀번호를 확인해주세요.")
else:
    print("아이디를 확인해주세요.")

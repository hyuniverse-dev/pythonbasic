from ch14.common import menu
from ch14.services import auth

'''
파일명: main.py
위치: .venv/ch14/
'''

### 웰컴투파이썬 실행파일

while True:
    user_input = menu.print_main_menu()

    if user_input == '1':
        # 회원가입 함수 호출
        auth.sign_up()
    elif user_input == '2':
        auth.sign_in()
    elif user_input == '3':
        break;
    else:
        print("메뉴를 다시 선택해주세요")

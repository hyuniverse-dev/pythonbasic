from ch14.common import menu
from ch14.services import auth, lotto

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
        auth.remove_user()
    elif user_input == '4':
        # 아이디와 비밀번호를 입력받아서 해당 회원이 정보를 조회하는 메뉴
        pass
    elif user_input == '5':
        # 로또 메일 발송 서비스
        lotto.send_lotto()
    elif user_input == '6':
        break;
    else:
        print("메뉴를 다시 선택해주세요")

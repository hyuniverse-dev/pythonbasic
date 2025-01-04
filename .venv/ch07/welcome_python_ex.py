'''
파일명: welcome_python_ex.py
위치: .venv/ch07/
'''
import auth
import menu
from custom_format import custom_print

user_id = ""
user_password = ""

while True:
    user_input = menu.print_main_menu()
    if user_input == "1":
        # 회원가입
        user_id, user_password = auth.insert_user()
        isSuccess = auth.sign_up(user_id, user_password)
        if isSuccess:
            custom_print("회원가입이 완료되었습니다.")
        else:
            custom_print(f"아이디와 비밀번호 입력을 확인해주세요. (ID: {user_id}, PASSWORD: {user_password})")
    elif user_input == "2":
        # 로그인 + 마이페이지
        if not user_id or not user_password:
            custom_print("회원가입을 해주세요.")
        else:
            input_id, input_password = auth.insert_user()
            if input_id == user_id and input_password == user_password:
                custom_print("로그인 되었습니다!")
                # 마이페이지 메뉴 실행
                while True:
                    user_input = menu.print_mypage_menu()
                    if user_input == "1":
                        auth.get_user_info(user_id, user_password)
                    elif user_input == "2":
                        user_id, user_password = auth.remove_user()
                        break
                    elif user_input == "3":
                        # 홈으로
                        break
                    else:
                        custom_print("메뉴를 다시 선택하세요.")
    elif user_input == "3":
        # 프로그램 종료
        break
    else:
        custom_print("메뉴를 다시 선택해주세요.")

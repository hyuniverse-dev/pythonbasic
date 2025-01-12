'''
파일명: menu.py
위치: .venv/ch07/
'''


def print_main_menu():
    '''
    메인 메뉴를 출력하는 함수
    
    :return: 
    '''
    print("<웰컴투 파이썬 버전2>")
    show_menus(["회원가입", "로그인", "회원탈퇴", "회원정보 조회","프로그램 종료"])
    user_input = input(">>>")
    return user_input


def print_mypage_menu():
    '''
    마이페이지 메뉴를 출력하는 함수
    
    :return: 
    '''
    print("<마이페이지>")
    show_menus(["회원 정보", "회원 탈퇴", "홈으로"])
    user_input = input(">>>")
    return user_input


def show_menus(menus: list):
    for index, menu in enumerate(menus, start=1):
        print(f"{index}.{menu}")

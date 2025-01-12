'''
파일명: auth.py
위치: .venv/ch14/services
설명: 사용자 인증과 관련된 함수
'''

from ch14.common.custom_format import custom_print
from ch14.models.user import User
from ch14.utils.helper import save_user, check_user, delete_user


def sign_up():
    input_id = input("아이디: ")
    input_password = input("비밀번호: ")
    input_name = input("이름: ")
    input_email = input("이메일: ")

    try:
        user = User(input_id, input_password, input_name, input_email)
        save_user(user)
    except ValueError as e:
        print(f"사용자 생성 실패: {e}")


def sign_in():
    input_id = input("아이디: ")
    input_password = input("비밀번호: ")
    check_user(input_id, input_password)


def remove_user():
    input_id = input("아이디: ")
    input_password = input("비밀번호: ")
    delete_user(input_id, input_password)


def get_user_info(user_id: str, user_password: str):
    '''
    사용자 정보를 조회하는 함수

    :param user_id:
    :param user_password:
    :return:
    '''
    custom_print(f"회원님의 아이디:{user_id}, 비밀번호:{user_password}")


def insert_user():
    '''
    사용자 정보를 입력받는 함수

    :return:
    '''
    user_id = input("아이디를 입력하세요 >>> ")
    user_password = input("비밀번호를 입력하세요 >>> ")
    return user_id, user_password

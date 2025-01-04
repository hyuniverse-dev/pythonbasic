'''
파일명: auth.py
위치: .venv/ch07/
'''

from custom_format import custom_print

def sign_up(user_id, user_password):
    '''
    전달받은 데이터를 검사해서 빈 문자열이 아니면 True 반환
    빈 문자열이면 False를 반환하는 함수

    :return: bool
    '''
    if user_id and user_password:
        return True
    else:
        return False


def get_user_info(user_id: str, user_password: str):
    '''
    사용자 정보를 조회하는 함수
    
    :param user_id:
    :param user_password:
    :return:
    '''
    custom_print(f"회원님의 아이디:{user_id}, 비밀번호:{user_password}")


def remove_user():
    '''
    사용자 정보를 삭제하는 함수
    
    :return: 
    '''
    custom_print("회원탈퇴가 되었습니다.")
    return "", ""


def insert_user():
    '''
    사용자 정보를 입력받는 함수

    :return:
    '''
    user_id = input("아이디를 입력하세요 >>> ")
    user_password = input("비밀번호를 입력하세요 >>> ")
    return user_id, user_password










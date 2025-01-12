'''
파일명: user.py
위치: .venv/ch14/models
설명: 사용자 정보를 생성하는 클래스
'''


class User:
    # 생성자
    def __init__(self, id: str, password: str, name: str, email: str):
        self.id = id
        self.password = password
        self.name = name
        self.email = email

        self.valid_values()
        self.valid_password()
        self.valid_email()

    def valid_values(self):
        if not self.id or not self.password or not self.email or not self.name:
            raise ValueError("필수값 입력이 누락됐습니다.")

    def valid_password(self):
        # (2) 비밀번호 정합성 검사 - 영어+숫자 조합
        has_digit = False
        has_alpha = False

        for word in self.password:
            if word.isdigit():
                has_digit = True
            if word.isalpha():
                has_alpha = True

        if not has_digit or not has_alpha:
            raise ValueError("비밀번호 형식이 올바르지 않습니다.")

        ### 리팩토링 (컴프리핸션 표현 방법으로 수정 가능)
        # if not any(word.isdigit() for word in self.password or word.isalpha() for word in self.password):
        #     raise ValueError("비밀번호 형식이 올바르지 않습니다.")

    def valid_email(self):
        # (1) 이메일 정합성 검사 - @, .
        if '@' not in self.email or '.' not in self.email:
            raise ValueError("이메일 형식이 올바르지 않습니다.")


# 테스트 코드 작성방법
if __name__ == "__main__":
    try:
        user = User("아이디", "password1", "이름", "email@email.com")
    except Exception as e:
        print(e)

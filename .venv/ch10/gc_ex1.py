'''
파일명: gc_ex1.py
위치: .venv/ch10/
'''

class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}이 생성되었습니다.")

    def __del__(self):
        print(f"{self.name}이 소멸되었습니다.")


# 1번
Test("옥순")
Test("영철")

print("프로그램이 종료되었습니다.")
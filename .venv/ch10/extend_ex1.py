'''
파일명: extend_ex1.py
위치: venv/ch10/
'''


# 상속
#   부모 클래스 생성
class Parent:
    def __init__(self):
        self.value = "Parent"
        print("부모 클래스 생성자가 호출되었습니다.")

    def parent_method(self):
        print("부모 클래스의 메소드가 호출되었습니다.")


class Child:
    def __init__(self):
        self.child_value = "Child"

    def child_method(self):
        print("자식 클래스의 메소드가 호출되었습니다.")

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


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_value = "Child"

    def child_method(self):
        print("자식 클래스의 메소드가 호출되었습니다.")


# Child 클래스로 인스턴스 생성
child = Child()

# Child 클래스의 필드와 메소드 호출
print(child.child_value)
child.child_method()

# Parent 클래스의 필드와 메소드 호출
print(child.value)
child.parent_method()
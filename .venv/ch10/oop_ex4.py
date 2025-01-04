'''
파일명: oop_ex4.py
위치: .venv/ch10/
'''


# Getter/Setter 데코레이터 사용하기
class Circle:

    def __init__(self, raduis):
        self.__raduis = raduis

    @property  # Getter 역할
    def radius(self):
        return self.__raduis

    @radius.setter  # Setter 역할
    def radius(self, radius):
        if radius >= 0:
            self.__raduis = radius
        else:
            print("음수는 대입할 수 없습니다.")


circle = Circle(10)

radius = circle.radius
print(radius)

circle.radius = -1
print(circle.radius)

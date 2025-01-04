'''
파일명: private_variable_ex1.py
위치: .venv/ch10/
'''


class Circle:
    def __init__(self, radius):
        if radius < 0:
            self.__radius = 0
        else:
            self.__radius = radius
        self.__name = "타원"

    # 원의 둘레를 구하는 메소드
    def get_circumference(self):
        return 2 * 3.14 * self.__radius

    # 원의 넓이 구하는 메소드
    def get_area(self):
        return 3.14 * (self.__radius ** 2)

    # 프라이빗 변수의 값을 반환하는 메소드를 정의 (Getter / 게터)
    def get_name(self):
        return self.__name

    # Setter / 세터
    def set_name(self, name):
        if name:
            self.__name = name
        else:
            print("빈 문자열은 대입이 불가능합니다.")

    # Setter
    def set_radius(self, radius):
        if radius < 0:
            print("0보다 작은 숫자는 허용하지 않습니다.")
        else:
            self.__radius = radius


circle1 = Circle(5)
print(circle1.get_circumference())
print(circle1.get_area())

print(circle1.get_name())

circle1.set_name("정원")
print(circle1.get_name())

######################
circle1.__name = "사각형"
print(circle1.get_name())
######################

print(circle1._Circle__name)
circle1._Circle__name = "삼각형"
print(circle1.get_name())

circle1.set_radius(-1)




'''
파일명: oop_practice1.py
위치: .venv/ch10/
'''


# NormalCar 클래스 정의
#   - 속성: 브랜드(brand), 색상(color)
#   - 메소드: normal_drive()
class NormalCar:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def normal_drive(self):
        print("일반모드로 주행합니다.")


# SportCar 클래스 정의
#   - 속성: 브랜드, 색상, 스포츠모드(is_sport_mode)
#   - 메소드: sport_drive()
class SportCar:
    def __init__(self, brand, color, is_sport_mode):
        self.brand = brand
        self.color = color
        self.is_sport_mode = is_sport_mode

    def sport_drive(self):
        if self.is_sport_mode:
            print("스포츠모드로 주행합니다.")
        else:
            print("일반모드로 주행합니다.")


# 객체 생성: 일반 자동차 2대, 스포츠 자동차 2대
cars = [
    NormalCar("현대", "블랙"),
    SportCar("람보르기니", "레드", True),
    NormalCar("기아", "화이트"),
    SportCar("포르쉐", "옐로우", True),
]

# cars 리스트를 순회하면서 NormalCar 인스턴스이면 normal_drive() 호출하고,
#                       SportCar 인스턴스이면 sport_drive() 호출하세요.
for car in cars:
    if isinstance(car, NormalCar):
        # NormalCar 인스턴스: normal_drive()
        car.normal_drive()
    elif isinstance(car, SportCar):
        # SportCar 인스턴스: sport_drive()
        car.sport_drive()

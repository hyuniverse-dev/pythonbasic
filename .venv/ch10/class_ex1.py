class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def sayHello(self):
        print(f"안녕하세요 저는 {self.name}입니다!")


student1 = Student("옥순", 87, 98, 90)
student1.sayHello()
print(id(student1))

student2 = Student("철수", 85, 90, 99)
student2.sayHello()
print(id(student2))











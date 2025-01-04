'''
파일명: loop_ex1.py
위치: .venv/ch06/
'''

# for i in range(100):
#     print("출력")

# 1. for문
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

colors = ["red", "blue", "green"]
for color in colors:
    print(color)

names = ["John", "Noah", "Isla"]
for name in names:
    print(f"-{name}")

# 2. while문
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. 반복문을 사용해서 remove() 함수 적용하기
numbers = [1, 2, 3, 1, 2, 3]
value = 1

while value in numbers:
    print(numbers)
    numbers.remove(value)

print(numbers)

print("###############################")

# 4. range()
#   - for문과 함께 자주 사용되는 범위 자료형

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print("반복문 실행")

for _ in range(5):
    print("반복문 실행")

#   - range()와 list() 함수로 새로운 리스트 만들기
list_a = []
list_b = list(range(1, 11))
print(list_b)










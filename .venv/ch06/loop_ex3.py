'''
파일명: loop_ex3.py
위치: .venv/ch06
'''

# 1. break 키워드
i = 0
while True:
    print(f"{i + 1}번째 반복입니다.")
    i += 1
    if i == 3:
        break

for i in range(5):
    print(f"{i + 1}번째 반복입니다.")
    if i == 3:
        break

while True:
    user_input = input("메세지를 입력하세요(quit은 종료) >>> ")
    if user_input == 'quit':
        break

# 2. continue 키워드
for i in range(5):
    if i == 2:
        continue
    print(f"{i + 1}번째 반복 실행")

# 3. pass 키워드
while True:
    pass

for i in range(5):
    pass

if 3 in numbers:
    pass

print("프로그램 종료")

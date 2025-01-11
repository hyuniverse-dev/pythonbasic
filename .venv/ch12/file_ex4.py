'''
파일명: file_ex4.py
위치: .venv/ch12/
'''

### 파일 읽기 (Read)
###     1.read() 2.readline() 3.readlines()

# date = input("검색 희망하는 스케쥴을 입력하세요(0000-00-00) >>> ")
date = "2025-01-05"
directory = f"../data/{date}.txt"

###     1.read() - 전체를 문자열 하나로 읽어오기
file = open(directory, 'rt', encoding='utf-8')

result = file.read()
print(type(result))
print(result)

file.close()

###     2.readline() - 한 줄 읽어오기
file = open(directory, 'rt', encoding='utf-8')

while True:
    result = file.readline()
    # "복습하기\n"
    if not result:
        break

    print(result, end="")

file.close()

print()

###     3.readlines()
line = int(input("검색할 줄의 개수를 이렵하세요 >>> "))

file = open(directory, 'rt', encoding='utf-8')

result = file.readlines()

for index, item in enumerate(result, start=1):
    # 3번째 줄까지만 출력
    if index <= line:
        print(item, end="")

file.close()

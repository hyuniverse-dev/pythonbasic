'''
파일명: file_ex6.py
위치: .venv/ch12/
'''

file_name = "황금별.txt"
directory = "../data/"

### (1) 황금별.txt 파일 열기 (read모드)
file = open(f"{directory}{file_name}", "rt", encoding='utf-8')

### (2) 파일로부터 불러들인 데이터를 읽어서 다음 단어가 몇 번 나오는지 찾기
###     - 지정 단어(1) 왕
###     - 지정 단어(2) 별
###     (2-1) readlines() 메소드로 텍스트 데이터 읽기
lyrics = file.readlines()
print(lyrics)

###     (2-2) for문으로 각 항목을 순회하면서 지정 단어 count 1씩 증가
count_king = 0
count_star = 0

for word in lyrics:
    for character in word:
        if "왕" == character:
            count_king += 1
        if "별" == character:
            count_star += 1

print(f"왕: {count_king}번, 별: {count_star}번")
file.close()

### 버전(2)
file = open(f"{directory}{file_name}", "rt", encoding="utf-8")

lyrics = file.read()

count_king = 0
count_star = 0
for word in lyrics:
    if "왕" == word:
        count_king += 1
    if "별" == word:
        count_star += 1

print(f"왕: {count_king}번, 별: {count_star}번")
file.close()



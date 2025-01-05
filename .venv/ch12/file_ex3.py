'''
파일명: file_ex3.py
위치: .venv/ch12/
'''

# 사용자로부터 입력받은 데이터를 txt 파일로 저장하기
import time

date = time.strftime("%Y-%m-%d")

file = open(f"../data/{date}.txt", "wt", encoding="utf-8")

while True:
    data = input("오늘의 스케쥴을 입력하세요 >>> ")

    if not data:
        break
    file.write(data + "\n")

file.close()
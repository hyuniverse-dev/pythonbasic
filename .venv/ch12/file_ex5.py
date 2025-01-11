'''
파일명: file_ex5.py
위치: .venv/ch12/
'''
import sys

date = '2025-01-05'
directory = f"../data/{date}.txt"

### sys 모듈 사용하기

file = open(directory, 'rt', encoding='utf-8')

words = file.readlines()

sys.stdout.writelines(words)

file.close()

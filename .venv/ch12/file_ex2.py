'''
파일명: file_ex2.py
위치: .venv/ch12/
'''

# 파일 추가

file = open("../data/hello.txt", "at", encoding='utf-8')

file.write("Hello.\n")
file.write("My name Oksoon")

print("hello.txt 파일에 내용이 추가되었습니다.")

file.close()

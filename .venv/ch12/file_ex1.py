'''
파일명: file_ex1.py
위치: .venv/ch12/
'''

# 파일 쓰기

file = open('../data/hello.txt', 'wt', encoding='utf-8')

file.write("안녕하세요.\n")
file.write("제 이름은 옥순입니다.\n")

print("hello.txt 파일이 생성되었습니다.")

file.close()

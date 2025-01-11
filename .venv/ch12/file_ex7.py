'''
파일명: file_ex7.py
위치: .venv/ch12/
'''

### with문
file_name = "황금별.txt"
directory = "../data/"

with open(f"{directory}{file_name}", "rt", encoding="utf-8") as file:
    lyrics = file.read()
    print(lyrics)

### with문으로 금칙어 필터링 프로그램 만들기
###     파일에서 텍스트 데이터를 읽어와서 특정 금칙어를 "*"로 치환하는 프로그램을 작성하세요.
###     치환할 때 기존 글자수만큼 "*"를 처리해주세요. (예시, 바보 -> **)
###     금칙어(1): 놈
###     금칙어(2): 바보
###     별 처리된 결과를 콘솔에 출력

filter_words = ["놈", "바보"]

with open(f"{directory}댓글.txt", "rt", encoding='utf-8') as file:
    content = file.read()

    # 금칙어 리스트에서 금칙어를 하나씩 가져와서 content에 해당 금칙어가 존재하는 경우 별처리
    for word in filter_words:
        content = content.replace(word, "*" * len(word))
        print(content)

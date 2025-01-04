'''
파일명: match_case_ex1.py
위치: .venv/ch04/
'''

# match-case문
#   Python 3.10.x 이상부터 사용 가능합니다.
#   패턴 매칭 기능을 제공하기 때문에 가독성을 높일 수 있습니다.

value = 10

if value == 10:
    print("value 변수의 값은 10입니다.")

match value:
    case 10:
        print("value 변수의 값은 10입니다.")

value = "Javascript"

# C, Java, Python 분기하기
if value == "C":
    print("C언어 입니다.")
elif value == "Java":
    print("Java 입니다.")
elif value == "Python":
    print("Python 입니다.")
else:
    print("새로운 언어입니다.")

match value:
    case "C":
        print("C언어 입니다.")
    case "Java":
        print("Java 입니다.")
    case "Python":
        print("Python 입니다.")
    case _:
        print("새로운 언어입니다.")

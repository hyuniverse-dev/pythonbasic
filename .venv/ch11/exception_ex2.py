'''
파일명: exception_ex2.py
위치: .venv/ch11/
'''

# 예외 처리 - 2

try:
    # 예외가 발생할 수 있는 코드
    input_number = int(input("숫자를 입력하세요 >>> "))
except:
    # 예외가 발생했을 때 실행할 코드
    print("숫자로 변환할 수 없는 데이터입니다.")
else:
    # 예외가 발생하지 않았을 때 실행할 코드
    print(f"입력받은 데이터: {input_number}")
finally:
    # 예외가 발생O/발생X 무조건 실행할 코드
    print("finally 블록이 실행됐습니다.")

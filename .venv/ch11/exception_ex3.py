'''
파일명: exception_ex3.py
위치: .venv/ch11/
'''

# 예외 객체 다루기

try:
    input_number = int(input("숫자를 입력하세요 >>> "))
except Exception as exception:
    print("예외가 발생했습니다!")
    print(f"예외 종류: {type(exception)}")
    print(exception)

print("::: 프로그램 종료 :::")

list_a = [52, 341, 200, 3817, 22]

try:
    input_index = int(input("인덱스 번호를 입력하세요 >>> "))
    print(f"{input_index}번째 요소: {list_a[input_index]}")

    ##### 새로운 예외 발생 코드 #####
    100 / input_index
    ##############################

except ValueError as exception:
    # (1)ValueError
    print(f"예외 종류: {type(exception)}")
    print(exception)
    print("숫자 데이터를 입력하세요.")
except IndexError as exception:
    # (2)IndexError
    print(f"예외 종류: {type(exception)}")
    print(exception)
    print(f"입력 가능 인덱스는 최대 {len(list_a) - 1}입니다.")
except Exception as exception:
    print(f"예외 종류: {type(exception)}")
    print(exception)
    print("알 수 없는 예외가 발생했습니다.")

print("::: 프로그램 종료 :::")

'''
파일명: function_ex3.py
위치: .venv/ch08/
'''

# 1. return 키워드
#   - 호출자에게 값을 반환해주는 키워드입니다.
def print_n_times(value, times):
    for i in range(times):
        print(value)
    return True


result = print_n_times("Hello World!", 3)

if result:
    print("print_n_times 함수 호출이 되었습니다.")


# 2. 함수의 영역
def test_function():
    list_a = [1, 2, 3]


# print(list_a) -> 함수 내부에서 선언된 변수는 함수 외부에서 참조 할 수 없습니다. return으로 값을 반환해야 외부에서 사용 가능합니다.

# 3. return 의 위치
#   - return 이후 코드는 실행되지 않습니다.
def test_function2():
    print("1번 위치입니다.")
    return True
    print("2번 위치입니다.")

test_function2()

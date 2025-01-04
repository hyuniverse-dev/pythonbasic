'''
파일명: function_ex4.py
위치: .venv/ch08/
'''


# 1. 두 개의 정수를 받아서 더한 결과를 반환하는 함수를 정의
def add_numbers(number1, number2):
    sum = number1 + number2
    return sum


# 2. 반환받은 결과를 출력하세요.
result = add_numbers(1, 2)
print(result)


# 3. 여러 개의 정수를 받아서 더한 결과를 반환하는 함수를 정의
def add_multi_numbers(*values):
    # sum = 0
    # for number in values:
    #     sum += number
    # return sum
    return sum(values)


# 4. 반환받은 결과를 출력하세요.
result = add_multi_numbers(10, 20, 30)
print(result)


# 5. 두 개의 정수를 받아서 더 큰 수를 반환하는 함수를 정의
def find_max_number(number1, number2):
    # if number1 > number2:
    #     return number1
    # else:
    #     return number2
    return number1 if number1 > number2 else number2


# 6. 반환받은 결과를 출력하세요.
result = find_max_number(99, 100)
print(result)


# 7. 리스트를 반환하는 함수 정의
def list_function(list_a: list):
    '''
    이 함수는 리스트를 반환하는 함수입니다.

    :param list_a:
    :return:
    '''
    list_a.append("추가 데이터")
    return list_a


my_list = ["기존 데이터1", "기존 데이터2", "기존 데이터3"]
result = list_function(my_list)
print(result)

# 8. 다음 빈칸을 채워서 사용자로부터 입력받은 여러 개의 정수 중
#    최대값과 최소값을 동시에 출력하는 프로그램을 완성하세요.

'''(조건)
		1. 사용자는 최소 2개 이상의 정수를 제한없이 프로그램이 실행되는 동안 무한히 입력할 수 있습니다.
		2. 사용자가 0을 입력하면 입력을 종료합니다.
		3. 입력받은 숫자는 리스트로 관리합니다.
		4. find_max_min_value 함수를 정의하고 사용자가 입력한 숫자 리스트를 매개변수로 받아
       함수 내에서 구한 최대값과 최소값을 호출자에게 반환합니다.
		5. 호출자는 반환받은 데이터를 다음 표준출력과 동일하게 출력합니다.


(표준입력)
		(테스트 케이스1)
		1번째 정수를 입력하세요.(종료는 0을 입력하세요.) >>> 
		2번째 정수를 입력하세요.(종료는 0을 입력하세요.) >>> 
		...
		n번재 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 

		(테스트 케이스2)
		1번째 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 123
		2번째 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 0

(표준출력)
		(테스트 케이스1)
		최대값: 113, 최소값: 1

		(테스트 케이스2)
		최소 2개 이상의 숫자를 입력하세요.'''

# 기본 import
import numbers_module

# 함수를 직접 사용할 수 있도록 import 하기
from numbers_module import find_max_min_value

numbers = []
count = 0

# 사용자로부터 데이터 입력받기
while True:
    number = int(
        input(f"{count + 1}번째 정수를 입력해주세요.(종료는 0을 입력해주세요.) >>>")
    )

    if number != 0:  # 0이 아닌 경우
        numbers.append(number)  # numbers 리스트에 추가
        count += 1  # count 변수 1 증가
    else:
        if count < 2:  # 2개 미만의 숫자를 입력한 경우
            print("최소 2개 이상의 숫자를 입력해주세요.")
        else:
            break

# 함수 호출하기
result = find_max_min_value(numbers)
print(f"최대값: {result[0]}, 최소값: {result[1]}")

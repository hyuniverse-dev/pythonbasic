'''
파일명: numbers.py
위치: .venv/ch08/
'''

# 함수 정의하기
def find_max_min_value(numbers: list):
    """
    주어진 숫자 리스트에서 최대값과 최소값을 찾아 반환합니다.

    Parameters:
    numbers (list): 숫자 리스트를 받는 매개변수입니다.

    Returns:
    list : 최대값과 최소값 리스트를 반환합니다.
    """

    max_value = numbers[0]  # 최대값 초기화
    min_value = numbers[0]  # 최소값 초기화

    for number in numbers:  # 각 요소에 대해 반복
        # find max_value
        if number > max_value:  # 최대값 찾기
            max_value = number
        # find min_value
        if number < min_value:  # 최소값 찾기
            min_value = number

    return [max_value, min_value]
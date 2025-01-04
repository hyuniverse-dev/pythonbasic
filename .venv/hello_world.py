# 함수 정의하기
def find_max_min_value(numbers):
    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        # find max_value
        if number > max_value:
            max_value = number
        # find min_value
        if number < min_value:
            min_value = number

    return [max_value, min_value]


numbers = []
count = 0

# 사용자로부터 데이터 입력받기
while True:
    number = int(input(f"{count + 1}번째 정수를 입력해주세요.(종료는 0을 입력해주세요.) >>>"))

    if number != 0:
        numbers.append(number)
        count += 1
    else:
        if count < 2:
            print("최소 2개 이상의 숫자를 입력해주세요.")
        else:
            break

# 함수 호출하기
result = find_max_min_value(numbers)
print(f"최대값: {result[0]}, 최소값: {result[1]}")
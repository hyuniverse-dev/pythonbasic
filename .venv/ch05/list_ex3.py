'''
파일명: list_ex3.py
위치: .venv/ch05/
'''

# 리스트의 다양한 사용법

# 1. sort() - 리스트를 정렬시켜주는 함수입니다.
numbers = [3, 1, 5, 289, 100]

# 1-1. 오름차순 정렬
numbers.sort()
print(numbers)

# 1-2. 내림차순 정렬
numbers.sort(reverse=True)
print(numbers)

print("#######################")

# 2. in / not in - 멤버십 연산자
#   - 특정 값이 리스트 내부에 있는지 확인하는 방법입니다.
#   - 값이 존재하면 True, 값이 존재하지 않으면 False
numbers = [2, 3, 4, 5, 1]
print(1 in numbers)  # True
print(1 not in numbers)  # False

# 3. index() 함수
#   - 특정 값의 인덱스를 찾아옵니다.
#   - 리스트에 특정 값이 존재하지 않으면 에러 발생합니다.
numbers = [2, 3, 4, 5, 1]
idx = numbers.index(3)
print(idx)

# idx = numbers.index(10)  # ValueError 발생
# print(idx)

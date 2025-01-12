'''
파일명: lotto_ex1.py
위치: .venv/ch15/
'''

import random

### 내장 모듈 실습 (로또 생성과 이메일 발송)

random_number = random.randint(1, 45)
print(random_number)

###     중복되지 않는 숫자 6개
numbers = []
while len(numbers) < 6:
    random_number = random.randint(1, 45)
    if random_number not in numbers:
        numbers.append(random_number)

print(numbers)  # 다음주 당첨 번호: [26, 31, 8, 11, 34, 9]

###     set 구조로 중복되지 않는 숫자 6개
numbers = set([1, 1, 1, 1, 2, 10])
print(numbers)

numbers = set()
while len(numbers) < 6:
    random_number = random.randint(1, 45)
    numbers.add(random_number)

print(list(numbers))








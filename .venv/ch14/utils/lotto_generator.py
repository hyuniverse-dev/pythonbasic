'''
파일명: lotto_generator.py
위치: ch14/utils/
'''

import random


def store_lotto():
    random_number = random.randint(1, 45)

    numbers = []
    while len(numbers) < 6:
        random_number = random.randint(1, 45)
        if random_number not in numbers:
            numbers.append(random_number)

    return numbers

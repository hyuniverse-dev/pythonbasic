'''
파일명: function_ex1.py
위치: .venv/ch08/
'''

# 내장 함수

# 1. enumerate()
#   - 리스트 자료랑 주로 사용하고, 리스트에 저장된 요소와 해당 요소의 인덱스를 함께 반환합니다.
#   - 반환타입은 이후에 배울 튜플(tuple)입니다.

list_a = ["a", "b", "c", "d"]
for index, character in enumerate(list_a, start=1):
    print(f"{index}. {character}")

# 2. sorted()
#   - sort() 함수랑 유사합니다. 정렬해주는 함수입니다.
#   - sort() 파괴적인 함수라 원본을 변형합니다.
list_b = ["c", "a", "b", "e"]
list_b2 = sorted(list_b)
print(list_b2)

list_b.sort()
print(list_b)











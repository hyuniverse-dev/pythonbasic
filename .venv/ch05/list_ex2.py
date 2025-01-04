'''
파일명: list_ex2.py
위치: .venv/ch05/
'''

# 1. 리스트와 연산자

# 1-1. + 연산자
#   - 두 개의 리스트 요소를 연결합니다.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b  # [1, 2, 3] + [4, 5, 6] -> [1, 2, 3, 4, 5, 6]
print(list_c)

# 1-2. * 연산자
#   - 두 개의 리스트 요소를 전개시킵니다.
#   - * 연사자가 [] 내부/외부에서 동작하는 원리가 다르기 때문에 주의해야 합니다.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [*list_a, *list_b]
print(list_c)

list_d = list_a * 3
print(list_d)

# 2. 리스트의 길이(요소의 개수) 구하기 - len()
list_a = [1, 2, 3, 4, 5]
length = len(list_a)
print(length)

print("#################################")

# 3. 리스트에 요소 추가하기

# 3-1. append() 함수
list_a = [1, 2, 3]
list_a.append(4)
print(list_a)

# 3-2. insert() 함수
list_a = [1, 2, 3]
list_a.insert(1, 4)
print(list_a)

# 3-3. extend() 함수
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)

print("#################################")

# 4. 리스트의 요소 삭제하기
#   - 인덱스로 삭제하기
#   - 값으로 삭제하기

# 4-1. del 키워드
list_a = [1, 2, 3]
del list_a[1]
print(list_a)

del list_a[0:]
print(list_a)

list_b = [1, 2, 3, 4, 5]
del list_b[:]
print(list_b)

# 4-2. pop()
#   - 제거한 값을 반환합니다.
#   - 인덱스를 지정하지 않으면 '-1' 로 간주하고, 마지막 요소를 삭제합니다.

list_a = [1, 2, 3]
value = list_a.pop(2)
print(list_a)
print(value)

value = list_a.pop()
print(list_a)
print(value)

# 4-3. remove() 함수
#   - 값을 기준으로 요소를 제거합니다.
#   - 만약 동일한 값이 여러 개 존재하면 인덱스가 빠른 값 1개만 삭제합니다.
list_a = [1, 2, 3, 1, 2, 3]
list_a.remove(1)
print(list_a) # [2, 3, 1, 2, 3]

list_a.remove(3)
print(list_a)

# 4-4. clear() 함수
list_a = [1, 2, 3]
list_a.clear()
print(list_a)














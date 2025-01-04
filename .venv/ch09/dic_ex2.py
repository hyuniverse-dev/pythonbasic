'''
파일명: dic_ex2.py
위치: .venv/ch09/
'''

# 딕셔너리와 다양한 함수들
user = {
    "name": "noah",
    "age": 20,
    "job": "developer"
}

# 1. len() - 딕셔너리의 키-값 쌍의 개수를 반환
res = len(user)
print(res)

# 2. clear() - 딕셔너리의 모든 항목을 제거
# user.clear()
print(user)

# 3. copy() - 딕셔너리의 복사본(얕은 복사)을 반환
copy_user = user.copy()
print(copy_user)

# 4. items() - 딕셔너리의 키-값을 튜플로 반환
res = user.items()
print(res)

# 5. keys() - 딕셔너리의 모든 키를 리스트로 반환
res = user.keys()
print(res)

# 6. values() - 모든 값을 리스트 형태로 반환
res = user.values()
print(res)

# 7. pop() - 지정된 키와 연결된 값을 제거 + 반환
res = user.pop("name")
print(res)

# 8. setdefault() - 키가 존재하지 않으면 전달한 인수를 추가
user.get("banana", "키가 존재하지 않습니다.")
print(user)

user.setdefault("banana", "키가 존재하지 않습니다.")
print(user)

##################################################

user = {
    "name": "noah",
    "age": 20,
    "job": "developer",
    "numbers": [1, 2, 3]
}
copy_user = user.copy()

print(user)
print(copy_user)

user["name"] = "isla"
print(user)
print(copy_user)

user["numbers"].append(4)
print(user)
print(copy_user)

copy_user["numbers"].append(5)
print(user)
print(copy_user)

list_a = [[1, 2], [3, 4], [5, 6], 100]
list_b = list_a.copy()

list_a[0][0] = 10
print(list_a)
print(list_b)

list_a[3] = 99
print(list_a)
print(list_b)

import copy

list_a = [[1, 2], [3, 4], [5, 6]]
list_b = copy.deepcopy(list_a)
print(list_a)
print(list_b)

list_a[0][0] = 100
print(list_a)
print(list_b)



















'''
파일명: dic_ex1.py
위치: .venv/ch09/
'''

# 딕셔너리 생성
my_dic = {
    "name": "박현",
    "gender": "남자",
    "age": 20,
    "hobbies": ["공부하기", "독서하기", "맛집가기"]
}

# 딕셔너리의 특정 키에 접근
name = my_dic["name"]
print(name)

# gender / age 키에 접근해서 값을 출력하기
gender = my_dic["gender"]
print(gender)

age = my_dic["age"]
print(age)

hobbies = my_dic["hobbies"]
print(hobbies)
for hobby in hobbies:
    print(hobby)

# 존재하지 않는 키에 접근하면 에러 발생
# my_dic["banana"]

# 딕셔너리에 새로운 값(키-쌍) 추가하기
my_dic["apple"] = "사과"
apple = my_dic["apple"]
print(apple)

# 딕셔너리의 기존 값 수정하기
my_dic["apple"] = "홍옥사과"
apple = my_dic["apple"]
print(apple)

# 딕셔너리의 기존 값 삭제하기
del my_dic["apple"]
print(my_dic)

isExist = "apple" in my_dic
print(isExist)

print(my_dic.get("apple", "키가 존재하지 않습니다."))





















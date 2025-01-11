import csv

'''
파일명: file2_ex2.py
위치: .venv/ch13/
'''

### csv 모듈 사용하기
with open("../data/회원정보.csv", "rt", encoding="utf-8") as file:
    members = []

    data = csv.reader(file)
    for item in data:
        members.append(item)

    print(members)

    for index, member in enumerate(members[1:]):
        if member[3] == '030-3333-3333':
            print(member)

print("=====================================")

with open("../data/동물병원현황.csv", "rt", encoding='utf-8') as file:
    keyword = input("동을 검색하세요 >>> ")
    names = []

    data = csv.reader(file)

    for item in data:
        if keyword in item[2]:
            names.append(item[1])

    print(names)

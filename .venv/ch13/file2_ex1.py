'''
파일명: file2_ex1.py
위치: .venv/ch13/
'''

### CSV 파일 다루기
###     쉼표로 값이 분리된 파일 형식
###     데이터베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식

### (1)모듈 없이 사용하기
###     split() - 특정 구분자에 따라서 데이터를 분리
alphabets = "a,b,c,d,e"
result = alphabets.split(",")
print(result)

###     (1-1) 회원정보.csv 파일 읽기
with open("../data/회원정보.csv", "rt", encoding='utf-8') as file:
    data = file.readlines()
    print(data)

    members = []

    for item in data:
        member = item.strip().split(",")
        members.append(member)

    print(members)

    ### 회원 이름 데이터만 출력하기
    for member in members[1:]:
        print(member[3])








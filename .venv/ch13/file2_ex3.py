import json

'''
파일명: file2_ex3.py
위치: .venv/ch13/
'''

### JSON 형식 파일 생성하기
members = [
    {
        "member_no": 1,
        "member_id": 'id1',
        "member_name": '옥순',
        "phone": '010-1111-1111'
    },
    {
        "member_no": 2,
        "member_id": 'id2',
        "member_name": '영자',
        "phone": '010-2222-2222'
    }
]

with open("../data/회원정보.json", "wt", encoding='utf-8') as file:
    json.dump(members, file, indent=4, ensure_ascii=False)  # JSON 객체를 파일에 직접 저장한다.

    print("회원정보.json 파일이 생성되었습니다.")


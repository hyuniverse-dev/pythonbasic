'''
파일명: helper.py
위치: .venv/ch14/utils
설명: 파일 생성 및 관리를 도와주는 함수
'''
from ch14.models.user import User


def save_user(user: User):
    # 기존 데이터 조회
    members = load_data_fromjson("./members.json")

    if len(members) < 1:
        members = []

    # 동일한 아이디 존재시
    for member in members:
        if member.get("id") == user.id:
            raise ValueError("아이디가 존재합니다.")

    members.append(user.__dict__)
    save_data_tojson("./members.json", members)  # 객체의 메소드를 제외한 속성만 추출 후 전달


def check_user(id: str, password: str):
    members = load_data_fromjson("./members.json")
    for member in members:
        if member.get("id") == id and member.get("password") == password:
            print(f"{member.get("id")}님 로그인 되었습니다.")
            return True
    raise ValueError("로그인 실패했습니다. (아이디 혹은 비밀번호를 확인해주세요.)")


def delete_user(id: str, password: str):
    # 기존 데이터 조회
    members = load_data_fromjson("./members.json")
    new_members = []

    # 전달받은 아이디랑 비밀번호가 일치하는 데이터 제외하고
    # 나머지 저장
    for member in members:
        if member.get("id") == id and member.get("password") == password:
            continue
        new_members.append(member)

    save_data_tojson("./members.json", new_members)


def save_data_tojson(path: str, data):
    import json
    '''
    전달받은 path 위치에 있는 파일에
    data를 JSON 형식으로 저장한다.
    '''
    with open(path, "wt", encoding="utf-8") as file:
        # 딕셔너리 -> JSON
        json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"{path} 에 데이터를 생성했습니다.")


def load_data_fromjson(path: str):
    import json
    '''
    전달받은 path 위치에 있는 파일의
    data를 파이썬 구조(리스트 안에 딕셔너리 담아서)로 반환한다.
    '''
    with open(path, 'rt', encoding='utf-8') as file:
        data = file.read()
        members = json.loads(data)
    return members

'''
파일명: list_ex4.py
위치: .venv/ch05/
'''

# 리스트 실습 문제(1)

# 다음은 A반 학생들의 명단입니다. 각 문제에 맞는 코드를 작성하세요.
class_a = ["현우", "지영", "동혁"]

# 1번. A반에 "상준"이가 전학을 왔습니다. 명단을 추가하는 코드를 작성하세요.
class_a.append("상준")
print(class_a)

# 2번. "현우"가 "현석"으로 이름을 개명했습니다. 명단의 이름을 수정하세요.
idx = class_a.index("현우")
class_a[idx] = "현석"
print(class_a)

# 3번. 이번주 청소 당번은 지영이와 동혁이 입니다. 슬라이싱을 사용해서 청소 당번을 출력하세요.
dangbun = class_a[1:3]
print(dangbun)

# 4번. 이번주 우유 당번은 명단의 마지막 학생입니다. 음수 인덱스를 사용해서 우유 당번을 출력하세요.
dangbun = class_a[-1]
print(dangbun)

# 5번. 기존의 A반에 B반 학생들을 합반하기로 했습니다. A반에 B반 학생들을 합반한 리스트를 만들어서 결과를 출력하세요.
class_a = ["현우", "지영", "동혁"]
class_b = ["삼영", "재석", "기영", "영자"]
class_a.extend(class_b)
print(class_a)

# 6번. 합쳐진 A반 학생들을 이름순으로 정렬하는 코드를 작성하고 결과를 출력하세요.
class_a.sort()
print(class_a)

# 7번. 합쳐진 A반에서 "동혁"이가 다른 학교로 전학을 갔습니다. 명단에서 제외한 결과를 출력하세요. (remove 함수 사용 권장)
class_a.remove("동혁")
print(class_a)

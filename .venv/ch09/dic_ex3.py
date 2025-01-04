'''
파일명: dic_ex3.py
위치: .venv/ch09/
'''

# 딕셔너리 실습문제

# 1. original_dic 생성(키: "name", "numbers", "job" / 값: "내이름", 리스트[1,2,3], 리스트["개발자","학생"])
original_dic = {
    "name": "박현",
    "numbers": [1, 2, 3],
    "job": ["개발자", "학생"]
}

# 2. 값 수정하기 - 이름을 영어로 수정하세요.
original_dic['name'] = "hyun park"

# 3. 값 추가하기 - 키: age / 값: 20 을 추가하세요.
original_dic['age'] = 20

# 4. 값 제거하기 - 키: "name" 을 제거하세요.
del original_dic['name']
# original_dic.pop('name')

# 5. original_dic 깊은 복사해서 copy_dic 생성하세요.
import copy

copy_dic = copy.deepcopy(original_dic)

# 6. copy_dic의 job 리스트에 "강사"를 추가하세요.
copy_dic['job'].append("강사")

# 7. original_dic, copy_dic 출력하세요.
print(original_dic)
print(copy_dic)






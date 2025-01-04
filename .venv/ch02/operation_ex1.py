'''
파일명: operation_ex1.py
위치: .venv/ch02/
'''

# 산술 연산자
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# 문자열 산술 연산자

tag1 = "#나는 솔로"
tag2 = "#솔로 탈출?"
tag3 = "#저는 최종 선택을 하지 않겠습니다."
tag = tag1 + tag2 + tag3
print(tag)

message = "아자!" * 3
print(message)

''' 문자데이터는 - 연산 불가능하다.
tag = tag1 - tag2
print(tag)
'''

# 복합대입연산자
x = 5
x += 3
# x = x + 3
print(x)

y = 10
y -= 2
# y = y - 2
print(y)

z = 7
z *= 4
# z = z * 4
print(z)

# 관계 연산자
#   - 불린값을 반환한다. (True / False)
print(1 > 6)
print(17 < 30)
print(9 <= 9)
print(8 >= 9)
print(10 == 10)
print(11 != 20)

print("파이썬" == "파잇썬")
print("7777" != "777")

# 논리 연산자
#   - 종류: and(그리고), or(또는), not(반전)

# and - 모든 조건이 True 여야지만 최종결과 True 반환
print((10 > 5) and (-1 < 0))
print(True and False)

# or - 하나의 조건만 True 여도 최종결과 True 반환
print(True or True)
print(True or False)

# not - 현재 값을 반전시킨다.
print(not True)
print(not False)

print("##### 퀴즈 #####")
'''
논리 연산자 퀴즈
    - 다음 결과를 예측하기
    1. True and True -> True
    2. Ture and False -> False
    3. False and False -> True 
    4. True or False -> True
    5. False or False -> Fasle
'''
print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(False or False)

# 논리 연산자의 우선순위 - not 연산자가 and / or 보다 먼저 수행된다.
print(not True and False or not False)

# 멤버십 연산자
#   - 시퀀스 자료형인 데이터에서 특정 데이터가 존재하는지 확안하는 연산자이다.
print("a" in "abc") # True
print("z" in "abc") # False
print("ac" not in "abc") # False

# 보너스
#   - x의 값이 0보다 크고, 10보다 작은 경우만 True를 반환한다.
#   - 파이썬에서는 범위를 연산할 때 일반 수학 표현식처럼 작성 가능하다.
x = 5
print(0 < x < 10)















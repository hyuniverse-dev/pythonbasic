'''
파일명: exception_ex1.py
위치: .venv/ch11/
'''

# 예외처리 - 1 (Exception/Error Handling)

#   예외 상황 발생시키기
print("::: 프로그램 시작 :::")

print("::: 사용자가 접속했습니다. :::")

print("::: 사용자가 주문 및 결제했습니다. :::")

# res = 10 / 0; # 문제(에러)가 발생하는 코드 기술

print("::: 주문내역을 데이터베이스에 저장했습니다. :::")

print("::: 프로그램 종료 :::")

##########   전통적인 예외 처리 방법 (if문 사용) ##########

number = input("숫자를 입력하세요 >>> ")

if number.isdigit():
    print(100 * int(number))

print("::: 프로그램 종료 :::")

#################### 끝 ####################

########## try - except 구문 ##########

try:
    number = int(input("숫자를 입력하세요 >>> "))
    print(100 * number)
except:
    print("입력한 값이 이상해요...ㅠ_ㅠ")

print("::: 프로그램 종료 :::")

#################### 끝 ####################


########## try - except 연습 ##########

# 입력받은 숫자로 100을 나누는 연산을 예외처리 구문을 사용해서 작성
try:
    number = int(input("숫자를 입력하세요 >>> "))
    print(100 / number)
except:
    print("입력한 값이 이상해요..ㅜ_ㅜ")

print("::: 프로그램 종료 :::")
#################### 끝 ####################


########## try - except 사용 예시 ##########

list_a = ["52", "273", "32", "apple", "103"]

# list_a 를 순회하면서 숫자 데이터만 float으로 타입캐스팅

list_b = []

for item in list_a:
    try:
        list_b.append(int(item))
    except:
        pass

print(f"{list_a} 중에서 숫자 데이터만 추출하면 {list_b}")


'''
파일명: lambda_ex1.py
위치: .venv/ch08/
'''

# 람다
#   - 이름이 없는 익명함수 입니다.
#   - 간단하게 함수를 정의할 수 있는 방법입니다.
#   - 주로 함수형 프로그래밍에서 함수의 인수로 전달하는 코드로 사용됩니다.

list_a = [1, 2, 3, 4, 5]

res = map(lambda x: x * x * x, list_a)
print(list(res))

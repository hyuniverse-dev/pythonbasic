'''
파일명: exception_practice2.py
위치: .venv/ch11/
'''

'''
✅ 다음 코드의 빈칸을 `try-except-else` 구문을 사용한 코드로 
채워서 예외가 발생하지 않고 코드가 실행 결과처럼 출력되도록 만들어주세요.

< 실행결과 >

첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 2
나누기 결과: 5.0

첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 0
0으로 나눌 수 없습니다.

첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: <문자>
숫자를 입력해 주세요!
'''

try:
    numerator = int(input("첫 번째 숫자를 입력하세요: "))
    denominator = int(input("두 번째 숫자를 입력하세요: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
except ValueError as e:
    print("숫자를 입력해 주세요!")
else:
  print("나누기 결과:", result)


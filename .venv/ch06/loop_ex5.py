'''
파일명: loop_ex5.py
위치: .venv/ch06/
'''

for i in range(2, 10):  # 외부 루프: 2단부터 9단까지 반복
    print(f"{i}단")
    for j in range(1, 10):  # 내부 루프: 1부터 9까지 반복
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # 각 구구단 출력 후 빈 줄 추가

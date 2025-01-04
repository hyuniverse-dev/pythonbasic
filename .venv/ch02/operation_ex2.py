'''
파일명: operation_ex2.py
위치: .venv/ch02
'''

# 문제: 다음 (?)을 채워서 두 자리 정수 45를 십의 자리와 일의 자리로 분리하세요.

'''
# number 변수를 선언하고 초기화 합니다.
number = 45

# 십의 자리와 일의 자리를 계산합니다.
tens = (?)  # 십의 자리를 구합니다.
units = (?)  # 일의 자리를 구합니다.

# 결과를 출력합니다.
print("십의 자리:", tens)
print("일의 자리:", units)
'''

number = 45

tens = number // 10
units = number % 10

print("십의 자리: ", tens)
print("일의 자리: ", units)

# ------------------------------------------------

# 문제: 3690초를 시, 분, 초로 변환하는 프로그램을 완성하세요.
#      (힌트: 1분은 60초이고, 1시간 60분)
'''
# total_seconds을 선언하고 초기화 합니다.
total_seconds = 3690

# 시간, 분, 초를 계산합니다.
hours = (?)  # 시간을 구합니다.
remaining_seconds = (?)  # 시간을 제외한 나머지 초를 구합니다.
minutes = (?) # 분을 구합니다.
seconds = (?) # 초를 구합니다.

# 결과를 출력합니다.
print("시:", hours)
print("분:", minutes)
print("초:", seconds)
'''

# total_seconds을 선언하고 초기화 합니다.
total_seconds = 3690
time_units = 60

# 시간, 분, 초를 계산합니다.
hours = total_seconds // (time_units * time_units)  # 시간을 구합니다.
remaining_seconds = total_seconds % (time_units * time_units)  # 시간을 제외한 나머지 초를 구합니다.
minutes = remaining_seconds // time_units # 분을 구합니다.
seconds = remaining_seconds % time_units # 초를 구합니다.

# 결과를 출력합니다.
print("시:", hours)
print("분:", minutes)
print("초:", seconds)

# f-strings
#   - 변수를 문자열 내에서 직접 사용하다.
#   - 변수는 {}로 감싼다.
print(hours, '시 ', minutes, '분 ', seconds, '초', sep='')
print(f'환산된 시간은: {hours}시 {minutes}분 {seconds}초')












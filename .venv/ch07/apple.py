'''
파일명: apple.py
위치: .venv/ch07/

테스트를 위한 파일입니다.
'''

# 리스트, 튜플 - 박싱과 언박싱
my_list = [1, 2, 3]
print(my_list)
a, b, c = my_list
print(a, b, c)

my_tuple = (1, 2, 3)
print(my_tuple)
d, e, f = my_tuple
print(d, e, f)

# 패킹 사용
my_tuple = 1, 2, 3, 4, 5
print(my_tuple)

a, *b, c = my_tuple
print(a, b, c)

# 튜플 함수
#   - sorted()
my_tuple = 99, 1, 41, 299, 300, -5
print(my_tuple)
sorted_list = sorted(my_tuple)
print(sorted_list)

my_list = [3, 1, 294, 287]
my_list.sort()
print(my_list)

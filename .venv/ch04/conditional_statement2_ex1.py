'''
파일명: conditional_statement2_ex1.py
위치: .venv/ch04/
'''

# 이중 중첩문(이중 if문)
number = 2

if number > 3:
    print("#####################")
    print("number는 3보다는 큽니다.")
    print("#####################")
    if number < 7:
        print("#####################")
        print("number는 3보다 크고, 7보다 작습니다.")
        print("#####################")
    else:
        print("#####################")
        print("number는 3보다 크고, 7보다 큽니다.")
        print("#####################")
else:
    print("#####################")
    print("number는 3보다 작습니다.")
    print("#####################")











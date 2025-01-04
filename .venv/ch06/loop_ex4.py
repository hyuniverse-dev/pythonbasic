'''
파일명: loop_ex4.py
위치: .venv/ch06/
'''

list_of_list = [[1, 2, 3], [4, 5, 6]]

for list in list_of_list:
    print(list)
    print("##########")
    for element in list:
        print(element)

'''
*
**
***
****
*****
******
*******
********
*********
'''
output = ""

for i in range(1, 10):
    for j in range(i):
        # 별 누적
        output += "*"
    output += "\n" # 2번

print(output)

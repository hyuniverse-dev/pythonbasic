from ch14.models import user

member = {
    "member_no": 1,
    "member_id": 'id1',
    "member_name": '옥순',
    "phone": '010-1111-1111'
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_a = [a % 2 == 0 for a in numbers]
print(list_a)

list_b = []
for number in numbers:
    list_b.append(number % 2 == 0)
print(list_b)
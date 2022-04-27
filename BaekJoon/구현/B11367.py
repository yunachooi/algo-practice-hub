t = int(input())

for _ in range(t):
    hobbit, score = map(str, input().split())

    if int(score) >=97:
        grade = "A+"
    elif int(score) >= 90:
        grade = "A"
    elif int(score) >= 87:
        grade = "B+"
    elif int(score) >= 80:
        grade = "B"
    elif int(score) >= 77:
        grade = "C+"
    elif int(score) >= 70:
        grade = "C"
    elif int(score) >= 67:
        grade = "D+"
    elif int(score) >= 60:
        grade = "D"
    else:
        grade = "F"

    print(hobbit, grade)

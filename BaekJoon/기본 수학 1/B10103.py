p1, p2 = 100, 100

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        p2 -= a
    elif a < b:
        p1 -= b

print(p1, p2, sep='\n')

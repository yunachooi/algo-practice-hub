t = int(input())

for _ in range(t):
    n = int(input())
    tc, tg, avg = 0, 0, 0   # total_credit, total_grade

    for _ in range(n):
        c, g = map(float, input().split())
        tc += c
        tg += c * g

    avg = tg / tc

    print(int(tc), '%.1f' % avg)

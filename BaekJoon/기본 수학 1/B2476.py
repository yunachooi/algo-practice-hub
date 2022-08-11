n = int(input())
maxprize = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c :
        maxprize = max(maxprize, 10000 + a * 1000)
    elif a == b or a == c :
        maxprize = max(maxprize, 1000 + a * 100)
    elif b == c :
        maxprize = max(maxprize, 1000 + b * 100)
    else:
        maxprize = max(maxprize, max(a, b, c) * 100)

print(maxprize)

from itertools import combinations

n, m = map(int, input().split())
num = list(map(int, input().split()))
res = 0

com = list(combinations(num, 3))

for i in com:
    if sum(i) <= m:
        res = max(res, sum(i))

print(res)

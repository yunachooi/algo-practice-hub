def d(n):
    n = n + sum(map(int, str(n)))
    return n

n = 10000
lst = list(range(n))

for i in range(n):
    if d(i) < n:
        lst[d(i)] = 0

for i in lst:
    if i != 0:
        print(i)

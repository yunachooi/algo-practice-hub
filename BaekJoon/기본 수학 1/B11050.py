n, k = map(int, input().split())
c = 1

for i in range(1, k + 1):
    c = c * (n - i + 1) / i
print(int(c))

n, k = map(int, input().split())
coin = list()
cnt = 0

for i in range(n):
    coin.append(int(input()))

for i in reversed(range(n)):
    cnt += k // coin[i]
    k = k % coin[i]

print(cnt)

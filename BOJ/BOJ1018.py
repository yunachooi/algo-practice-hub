N = int(input())
M = [int(x) + N for x in input().split()]
MAX = max(M) + 1 - N
cnt = 0

for i in range(N):
    if M[i] > MAX:
        cnt += 1

print(cnt)

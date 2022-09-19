import sys
input = sys.stdin.readline  #시간 초과 방지

n = int(input())

f = [0] * (n + 1)
f[1] = 1

for i in range(2, n + 1):
    f[i] = f[i - 1] + f[i - 2]

print(f[n])

import sys
input = sys.stdin.readline  #시간 초과 방지

n = int(input())
total = 0

for _ in range(n):
    total += int(input())

print(total - (n - 1))

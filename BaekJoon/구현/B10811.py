import sys

n, m = map(int, sys.stdin.readline().split())

list = []

for i in range(n + 1):
    list.append(i)

for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    tmp = list[i : j + 1]
    tmp.reverse()
    del list[i : j + 1]
    list[i:i] = tmp

print(*list[1:])

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = dict()
for i in range(n):
    name = input().rstrip()
    d[name] = str(i+1)
    d[str(i+1)] = name

print(*[d[input().rstrip()] for _ in range(m)],sep="\n")

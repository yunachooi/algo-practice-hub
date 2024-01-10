import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter' : s.add(name)
    elif status == 'leave' : s.remove(name)

print(*sorted(list(s))[ : : -1], sep = '\n')

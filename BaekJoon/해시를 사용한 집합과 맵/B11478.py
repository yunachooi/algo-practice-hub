import sys
input = sys.stdin.readline

s = input().rstrip()
r = set()

for i in range(len(s)):
    for j in range(i, len(s) + 1):
        r.add(s[i : j + 1])

print(len(r))

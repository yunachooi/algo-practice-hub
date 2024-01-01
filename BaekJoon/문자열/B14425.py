n, m = map(int, input().split())
s = []
a = 0

for i in range(n):
    s.append(input())

for i in range(m):
    b = input()

    if b in s:
        a += 1

print(a)

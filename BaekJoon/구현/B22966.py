n = int(input())
t = []; d = [] # text, digit

for i in range(n):
    a, b = map(str, input().split())
    t.append(a)
    d.append(b)

print(t[d.index(min(d))])

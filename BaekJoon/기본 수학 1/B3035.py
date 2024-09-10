a, b, c, d = map(int,input().split())
p = []
scan = []

for i in range(a):
    p.append(input())

for i in range(a):
    re = []
    
    for k in range(b):
        re.append(p[i][k] * d)

    for h in range(c):
        scan.append(re)

for s in scan:
    print(''.join(s))

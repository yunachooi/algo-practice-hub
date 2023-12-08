n = int(input())
xlist = []
ylist = []

for i in range(n):
    x, y = map(int, input().split())
    
    xlist.append(x)
    ylist.append(y)

print((max(xlist) - min(xlist)) * (max(ylist) - min(ylist)))

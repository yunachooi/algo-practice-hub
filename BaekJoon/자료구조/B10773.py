import sys
input = sys.stdin.readline

k = int(input())
x = []
y = 0

for i in range(0, k):
    a = int(input())
    
    x.append(a)
    if x[-1] == 0:
        del x[-1]
        del x[-1]
        
l = len(x)

for i in range(0, l):
    y += x[i]
    
print(y)

n, m = map(int,input().split())
lst = []

for i in range(n):
    lst.append(i+1)
    
for i in range(m):
    a, b = map(int,input().split())
    
    l = lst[a - 1]
    lst[a - 1] = lst[b - 1]
    lst[b - 1] = l
    
for i in lst:
    print(i, end = ' ')

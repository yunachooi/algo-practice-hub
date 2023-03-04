n, m = map(int,input().split())
lst = [0] * n

for i in range (m) :
    a, b, c = map(int,input().split())
    
    for j in range (a, b + 1, 1) :
        lst[j - 1] = c
        
for i in range (n) :
    print(lst[i], '', end='')

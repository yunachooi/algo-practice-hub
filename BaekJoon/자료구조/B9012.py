import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = list(input())
    a = 0
    b = 0
    
    for j in range(len(x)):
        if x[j] == '(':
            a += 1
            
        elif x[j] == ')':
            b += 1
            
        if a < b:
            print('NO')
            break
        
    if a == b:
        print('YES')
        
    elif a > b:
        print('NO')

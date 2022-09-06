n = int(input())
cnt = 0

for i in range(n * 2 - 1):
    if i < n:
        cnt += 1
        
    else: cnt -= 1
    
    print(' '* (n - cnt) + '*' * (cnt * 2 - 1))

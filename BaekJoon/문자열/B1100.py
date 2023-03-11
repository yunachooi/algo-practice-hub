cnt = 0

for i in range(8):
    n = input()
    
    if i % 2 : 
        for j in range(1, len(n), 2):
            if n[j] == 'F':
                cnt += 1

    else:
        for j in range(0, len(n) - 1, 2):
            if n[j] == 'F':
                cnt += 1

print(cnt)

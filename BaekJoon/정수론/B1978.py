n = int(input())
lst = map(int, input().split())

cnt = 0

for i in lst:
    for j in range(2, i + 1):
        if i % j == 0:
            if j == i:
                cnt += 1
            break

print(cnt)
    

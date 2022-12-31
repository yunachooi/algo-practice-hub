n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i <= 99 :
        cnt += 1

    else:
        n = list(map(int, str(i)))
        if n[0] - n[1] == n[1] - n[2]:
            cnt += 1
            
print(cnt)

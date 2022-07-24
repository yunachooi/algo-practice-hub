n = str(input())
cnt = 0

for i in range(len(n)) :
    if cnt < 9 :
        print(n[i], end = "")
        cnt += 1
    elif cnt == 9 :
        print(n[i])
        cnt = 0

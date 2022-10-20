k = int(input())

for _ in range(k):
    p, m = map(int, input().split())    #참가자의 수, 자리의 수
    s, cnt = [False] * 501, 0

    for _ in range(p):
        j = int(input().strip())
        
        if not s[j]:
            s[j] = True
        else :
            cnt += 1

    print(cnt)

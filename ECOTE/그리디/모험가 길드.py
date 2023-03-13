n = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 0
cnt = 0

for i in lst:
    cnt += 1

    if cnt >= i:
        answer += 1
        cnt = 0

print(answer)

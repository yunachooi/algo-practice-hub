t = int(input())

answer = map(int, input().split())
cnt = 0

for i in answer:
    if i == t:
        cnt += 1

print(cnt)

    

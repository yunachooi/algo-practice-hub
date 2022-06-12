day = int(input())
car = [int(x) for x in input().split()]
cnt = 0

for i in range(5):
    if day == car[i]:
        cnt += 1

print(cnt)

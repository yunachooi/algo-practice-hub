import sys
input = sys.stdin.readline  #시간 초과 방지

m = int(input())
n = int(input())

lst = []

for i in range(m, n + 1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break

    if cnt == 0 and i != 1:
        lst.append(i)

if lst:
    print(sum(lst))
    print(min(lst))

else:
    print(-1)

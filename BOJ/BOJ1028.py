n = int(input())
T = input().split()
for i in range(n):
    T[i] = int(T[i])

cnt = 0
maxT = 0

for i in range(n):
    if T[i] < 25:
        cnt = 0
    else :
        cnt += 1
        if cnt > maxT:
            maxT = cnt

print(maxT)

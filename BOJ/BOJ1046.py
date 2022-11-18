N = int(input())
H = list(map(int, input().split(' ')))

for i in range(N):
    maxN = 0
    for j in range(i, -1, -1):
        if H[j] > H[i]:
            maxN = j + 1
            break
    print(maxN, end = ' ')

data = input().split()
n = int(data[0]) + 1
m = int(data[1]) + 1

M = [[0 for j in range(m)] for i in range(n)]

for i in range(1, n):
    data = input().split()
    for j in range(1, m):
        M[i][j] = int(data[j-1])

k = int(input())
Q = [[0, 0, 0, 0] for i in range(k)]

for i in range(k):
    data = input().split()
    for j in range(4):
        Q[i][j] = int(data[j])

for i in range(1, n):
    for j in range(2, m):
            M[i][j] += M[i][j-1]
                      
for i in range(2, n):
    for j in range(1,m):
            M[i][j] += M[i-1][j]

for a in range(k):
    i, j, x, y = Q[a][0], Q[a][1], Q[a][2], Q[a][3]
    value = M[x][y] - M[x][j-1] -  M[i-1][y] + M[i-1][j-1]
    print(value)

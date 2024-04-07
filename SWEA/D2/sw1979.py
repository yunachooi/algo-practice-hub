T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    res = 0

    # 가로
    for i in range(n):
        tmp = 0
        for j in range(n):
            if graph[i][j] == 1:
                tmp += 1
            else:
                if tmp == k:
                    res += 1
                tmp = 0
                
        if tmp == k:
            res += 1

    # 세로
    for j in range(n):
        tmp = 0
        for i in range(n):
            if graph[i][j] == 1:
                tmp += 1
            else:
                if tmp == k:
                    res += 1
                tmp = 0
                
        if tmp == k:
            res += 1

    print('#{} {}'.format(t, res))

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0

    for i in range(N):
        for j in range(N):
            SUM = 0

            for x in range(M):
                for y in range(M):
                    if not (i + x >= N or j + y >= N):
                        SUM += graph[i + x][j + y]

            MAX = max(MAX, SUM)

    print(f'#{test_case} {MAX}')

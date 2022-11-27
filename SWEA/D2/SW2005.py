T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f'#{test_case}')
    
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end = ' ')
        print()

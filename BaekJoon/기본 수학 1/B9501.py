T = int(input())

for _ in range(T):
    result = 0
    N, D = map(int, input().split())

    for _ in range(N):
        v, f, c = map(int, input().split())

        if (f / c) * v >= D:
            result += 1
            
    print(result)

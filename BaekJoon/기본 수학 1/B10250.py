T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    x, y = 0, 0

    if N % H == 0:
        x = N // H
        y = H * 100
    else:
        x = N // H + 1
        y = N % H * 100

    print(x + y)

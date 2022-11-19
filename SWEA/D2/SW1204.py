T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    graph = [int(x) for x in input().split()]
    cnt = [0] * 101
    MAX, idx = 0, 0

    for i in range(1000):
        cnt[graph[i]] += 1

    for i in range(101):
        if cnt[i] >= MAX:
            MAX = cnt[i]
            idx = i

    print(f'#{N} {idx}')

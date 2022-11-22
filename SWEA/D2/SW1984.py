T = int(input())

for test_case in range(1, T + 1):
    graph = [int(x) for x in input().split()]

    avg = round((sum(graph) - max(graph) - min(graph)) / 8)

    print(f'#{test_case} {avg}')

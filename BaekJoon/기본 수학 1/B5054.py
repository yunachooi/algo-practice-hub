t = int(input())

for _ in range(t):
    n = int(input())    # 상점의 수
    lst = list(map(int, input().split()))

    print((max(lst) - min(lst)) * 2)

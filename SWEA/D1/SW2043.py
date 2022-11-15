P, K = map(int, input().split())

if P >= K:
    print(P - K + 1)
else:
    print(P + 1000) - K

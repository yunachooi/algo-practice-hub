n = int(input())
ns = set(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

for i in ms:
    if i in ns:
        print(1)
    else:
        print(0)

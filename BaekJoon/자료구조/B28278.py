import sys

n = int(input())
arr = list()

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))

    match a[0]:
        case 1:
            arr.append(a[1])
        case 2:
            if not arr :
                print(-1)
            else :
                print(arr.pop())
        case 3:
            print(len(arr))
        case 4:
            if arr :
                print(0)
            else :
                print(1)
        case 5:
            if not arr:
                print(-1)
            else :
                print(arr[-1])

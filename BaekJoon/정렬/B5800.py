import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(f'Class {i + 1}')

    tmp = list(map(int, input().split()))
    gap = 0
    arr = tmp[1 : ]

    arr.sort(reverse = True)

    for j in range(1, tmp[0]):
        gap = max(gap, arr[j - 1] - arr[j])

    print(f'Max {arr[0]}, Min {arr[-1]}, Largest gap {gap}')

import sys
input = sys.stdin.readline

T = int(input())
num = [ [10, 10, 10, 10], [1, 1, 1, 1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4, 6, 4], [5, 5, 5, 5], [6, 6, 6, 6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9, 1, 9] ]

for _ in range(T):
    a, b = map(int, input().split())

    a %= 10
    b %= 4

    print(num[a][b])

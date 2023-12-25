import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(int(input()))]

for x, y in sorted(lst):
    print(x, y)

import sys
t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())   #  시간초과 해결
    print(int(n)**2)

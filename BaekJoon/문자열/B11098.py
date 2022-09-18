import sys
input = sys.stdin.readline  #시간 초과 방지

n = int(input())

for _ in range(n):
    p = int(input())    #고려해야될 선수
    maxc = 0

    for _ in range(p):
        c, name = input().split()    #선수 정보(비용, 이름)
        c = int(c)

        if maxc < c:
            maxc = c
            player = name

    print(player)

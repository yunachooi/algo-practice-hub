import copy
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def spread_virus(dmaps, virus):
    global ans

    que = deque(virus)
    while que:
        q = que.popleft()
        x, y = q[0], q[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if dmaps[nx][ny] == 0:
                    dmaps[nx][ny] = 2
                    que.append([nx, ny])


    safe_range = 0
    for i_dmaps in dmaps:
        safe_range += i_dmaps.count(0)
    ans = max(ans, safe_range)


def set_wall(maps, empty, virus):
    l = len(empty)
    for i in range(l):
        for j in range(i):
            for k in range(j):
                maps[empty[i][0]][empty[i][1]] = 1
                maps[empty[j][0]][empty[j][1]] = 1
                maps[empty[k][0]][empty[k][1]] = 1

                deep_maps = copy.deepcopy(maps)
                spread_virus(deep_maps, virus)

                maps[empty[i][0]][empty[i][1]] = 0
                maps[empty[j][0]][empty[j][1]] = 0
                maps[empty[k][0]][empty[k][1]] = 0


N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

empty, virus = [], []
for x in range(N):
    for y in range(M):
        if maps[x][y] == 0:
            empty.append([x, y])
        elif maps[x][y] == 2:
            virus.append([x, y])
ans = 0
set_wall(maps, empty, virus)
print(ans)

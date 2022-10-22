n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    #주어진 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x, y - 1) #상
        dfs(x, y + 1) #하
        dfs(x - 1, y) #좌
        dfs(x + 1, y) #우
        return True
    return False

#main Program#
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)

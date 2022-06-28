n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
# 현재 x, y 좌표 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))

# 0 = 육지, 1 = 바다

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


'''main'''

# 동, 서, 남, 북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn_time = 0

while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 정면에 미방문 칸 존재 시
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    # 회전 후 미 방문 칸이 없거나 바다인 경우
    else :
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 이동이 가능한 경우
        if arr[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0

print(cnt)

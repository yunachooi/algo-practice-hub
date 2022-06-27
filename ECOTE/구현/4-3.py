# 현재 나이트의 위치
knight = input()
row = int(knight[1])
col = int(ord(knight[0])) - int(ord('a')) + 1
        # ord = 단일 문자의 아스키 값 반환

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동 여부 파악
cnt = 0
for step in steps:
    # 이동 위치 파악
    next_row = row + step[0]
    next_col = col + step[1]

    # 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)

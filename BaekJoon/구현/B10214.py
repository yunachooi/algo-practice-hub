t = int(input())
score_y, score_k = 0, 0

for _ in range(t):
    for _ in range(9):
        y, k = map(int, input().split())
        score_y += y
        score_k += k

    if score_y > score_k:   # 연세대가 이긴 경우
        print('Yonsei')

    elif socre_k > score_y: # 고려대가 이긴 경우
        print('Korea')

    else:   # 비긴 경우
        print('Draw')

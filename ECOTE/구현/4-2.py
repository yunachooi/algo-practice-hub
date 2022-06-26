# 시(hour) 입력받기
n = int(input())
cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각에 '3'이 포함되어 있다면 카운트
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

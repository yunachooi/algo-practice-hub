n, m, k = map(int, input().split())
data = list(map(int, input().split())) # N개의 수를 공백 구분

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 작은 수

# 가장 큰 수가 더해지는 횟수 계산
count = (int(m / (k + 1)) * k) + m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)

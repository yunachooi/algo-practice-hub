X = int(input())
N = int(input())
sumX = 0

for i in range(N):
    a, b = map(int, input().split())
    sumX += a * b

if X == sumX:
    print('Yes')
else:
    print('No')

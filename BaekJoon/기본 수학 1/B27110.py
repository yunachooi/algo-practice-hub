n = int(input())
lst = list(map(int, input().split()))
result = 0

for i in range(3):
    if lst[i] <= n:
        result += lst[i]
    else:
        result += n

print(result)

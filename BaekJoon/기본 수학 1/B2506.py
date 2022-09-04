n = int(input())
lst = list(map(int, input().split()))
combo, result = 0, 0

for i in lst:
    if i == 1:
        result += i + combo
        combo += 1
    else:
        combo = 0

print(result)

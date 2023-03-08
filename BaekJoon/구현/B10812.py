n, m = map(int, input().split())
lst = [i + 1 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    
    lst[i - 1 : j] = lst[k - 1 : j] + lst[i - 1 : k - 1]

print(*lst)

n = int(input())
a, b = map(int, input().split())
total = a // 2 + b

print(min(total, n))

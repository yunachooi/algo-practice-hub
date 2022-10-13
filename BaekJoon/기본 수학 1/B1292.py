a, b = map(int, input().split())
lst = []

for i in range(1, 50):
    lst += [i] * i

print(sum(lst[a - 1 : b]))

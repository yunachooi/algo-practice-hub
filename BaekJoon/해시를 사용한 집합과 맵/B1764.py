n, m = map(int, input().split())
a = set()
b = set()

for i in range(n):
    a.add(input())

for i in range(m):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)

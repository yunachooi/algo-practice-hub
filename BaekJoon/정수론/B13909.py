n = int(input())
r, c = 0, 1

while(c <= n):
    r += 1
    c = (r + 1) ** 2

print(r)

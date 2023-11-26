n, b = map(str, input().split())
n = n[::-1]
b = int(b)
con = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0

for i, j in enumerate(n):
    ans += (con.index(j) * b ** i)

print(ans)

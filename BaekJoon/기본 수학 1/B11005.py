n, b = map(int,input().split())
r = ''
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n:
    r += str(s[n % b])
    n //= b
print(r[::-1])

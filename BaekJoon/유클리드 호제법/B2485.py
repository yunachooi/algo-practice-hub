from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
g = 0
for i in range(n):
    a = int(input())
    if i == 1:
        g = a - b
    elif i > 1:
        g = gcd(g, a - b)
    b = a

    if i == 0: num1 = a
    elif i == n-1: num2 = a

cnt = (num2 - num1 + g) // g - n

print(cnt)

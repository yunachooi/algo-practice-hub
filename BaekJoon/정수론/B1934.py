n = int(input())
result = 0

def gcd(a, b):  # 최소공배수
    while b != 0:
        a, b = b, a % b
    return a

for i in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))

import sys
input = sys.stdin.readline  #시간 초과 방지

total = int(input())

for _ in range(9):
    price = int(input())
    total -= price

print(total)

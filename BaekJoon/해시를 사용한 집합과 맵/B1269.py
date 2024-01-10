import sys
input = sys.stdin.readline

an, bn = map(int, input().split())

a = set(sys.stdin.readline().rstrip().split())
b = set(sys.stdin.readline().rstrip().split())

print(len(a ^ b))

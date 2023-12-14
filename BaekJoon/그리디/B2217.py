import sys
input = sys.stdin.readline

n = int(input())
rope = []
max = 0
j = n

for _ in range(n):
    rope.append(int(input()))

rope.sort()

for i in range(0, n):
    if max < rope[i] * j:
        max = rope[i] * j
    j -= 1

print(max)

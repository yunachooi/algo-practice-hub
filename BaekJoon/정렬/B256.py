import sys
input = sys.stdin.readline

n = int(input())
l = [[0 for i in range(101)] for i in range(101)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(10):
        for k in range(10):
            l[a + j][b + k] = 1
            
count = 0

for i in l:
    for j in i:
        if j == 1:
            count += 1
            
print(count)

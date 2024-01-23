import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
d = deque()

for i in range(n):
    l = list(map(int, input().strip().split()))
    t = l[0]
    f = len(d)
    
    if t == 1:
        d.appendleft(l[1])
    elif t == 2:
        d.append(l[1])
    elif t == 3:
        print(d.popleft() if f else -1)
    elif t == 4:
        print(d.pop() if f else -1)
    elif t == 5:
        print(len(d))
    elif t == 6:
        print(0 if f else 1)
    elif t == 7:
        print(d[0] if f else -1)
    elif t == 8:
        print(d[-1] if f else -1)

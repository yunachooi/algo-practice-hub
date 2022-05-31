from heapq import *
import sys
input = sys.stdin.readline

L = []
R = []
n = int(input())

for i in range(n):
    x = int(input())
    
    if i % 2 == 0:
        if len(R) > 0 and R[0] < x:
            heappush(L, (-R[0], R[0]))
            heappop(R)
            heappush(R, x)
        else:
            heappush(L, (-x, x))
            
    else:
        if len(L) > 0 and L[0][1] > x:
            heappush(R, L[0][1])
            heappop(L)
            heappush(L, (-x, x))
        else:
            heappush(R, x)
            
    print(L[0][1])

from heapq import *
import sys
input = sys.stdin.readline

L = []
n = int(input())

for i in range (n):
    x = int(input())

    if x == 0:
        if len(L) == 0:
            print(0)
        else:
            print(heappop(L)[1])
            
    else: # x != 0
        heappush(L, [abs(x), x])

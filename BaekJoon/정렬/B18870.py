import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = set(nums)

s = sorted(s)
d = dict()

for i, v in enumerate(s): 
    d[v] = i
    
print(*[d[x] for x in nums])  

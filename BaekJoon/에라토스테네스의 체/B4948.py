import sys
input = sys.stdin.readline

maxn = 123456*2 + 1
s = [True]*maxn
s[0] = s[1] = False

for i in range(2, maxn):
        if s[i]:
            j = 2
            while i * j < maxn:
                   s[i * j] = False
                   j += 1

while 1:
    m = int(input().rstrip())
    
    if m == 0:
        break
        
    n = m * 2
    print(len([i for i in range(m + 1, n + 1) if s[i]]))

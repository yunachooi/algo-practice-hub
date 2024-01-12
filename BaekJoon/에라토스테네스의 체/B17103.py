import sys
input = sys.stdin.readline

maxn = 1000000 + 1
s = [True] * maxn
s[0] = s[1] = False
t = int(input().rstrip())

for i in range(2, maxn):
        if s[i]:
            j = 2
            
            while i * j < maxn:
                   s[i * j] = False
                   j += 1

for _ in range(t):
    n = int(input().rstrip())
    cnt = 0
    
    for i in range(2, n // 2 + 1):
          if s[i] and s[n - i]: cnt += 1
    print(cnt)

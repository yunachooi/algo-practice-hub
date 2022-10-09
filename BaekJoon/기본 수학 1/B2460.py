p , maxp = 0, 0

for _ in range (10):
    o, i = map(int, input().split())    # out, in
    
    p += i - o  # people
    
    maxp = max(p, maxp)

print(maxp)

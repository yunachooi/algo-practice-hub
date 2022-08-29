result, maxr = 0, 0

for _ in range(4):
    o, i = map(int, input().split())    # out, in

    result -= o
    result += i
    
    maxr = max(maxr, result)

print(maxr)
    

t = int(input())

for _ in range(t):
    l = list(map(int, input().split()))
    even = []
    
    for i in l:
        if i % 2 == 0:
            even.append(i)

    print(sum(even), min(even))

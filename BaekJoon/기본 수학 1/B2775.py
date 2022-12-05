T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    lst = [i + 1 for i in range(n)]
    
    for _ in range(0, k):
        for i in range(0, n):
            lst.append(sum(lst[:i+1]))
            
        for _ in range(0, n):
            del lst[0]
    print(lst[-1])

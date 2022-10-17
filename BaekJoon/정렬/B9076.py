t = int(input())

for _ in range(t):
    lst = list(map(int, input().split()))

    lst.remove(max(lst))
    lst.remove(min(lst))

    if max(lst) >= min(lst) + 4:
        print('KIN')
        
    else:
        print(sum(lst))

lst = []

for _ in range(9):
    n = int(input())
    lst.append(n)

for i in range(9):
    for j in range(i + 1,9):
        if sum(lst) - lst[i] - lst[j] == 100:
            a = lst[i]
            b = lst[j]
            break
        
lst.remove(a)
lst.remove(b)

print('\n'.join(map(str, sorted(lst))))

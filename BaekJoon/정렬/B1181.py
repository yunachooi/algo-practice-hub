n = int(input())
lst = [] * n

for i in range(n):
    lst.append(input())

lst = sorted(list(set(lst)))

for i in range(len(lst)):
    lst[i] = (lst[i], len(lst[i]))

lst.sort(key = lambda x: x[1])

for i in lst:
    print(i[0])

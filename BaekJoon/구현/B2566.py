lst = []

for i in range(9):
    lst.append(list(map(int, input().split(' '))))

n = 0
arr = 0
for i in range(9):
    for j in range(9):
        if n <= lst[i][j]:
            n = lst[i][j]
            arr = [i, j]
print(n)
print(arr[0]+1, arr[1]+1)

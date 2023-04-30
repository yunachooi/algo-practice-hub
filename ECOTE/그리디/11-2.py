lst = input()
result = int(lst[0])

for i in range(1, len(lst)):
    n = int(lst[i])

    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

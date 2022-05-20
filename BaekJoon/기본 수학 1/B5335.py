T = int(input())

for i in range(T):
    case = input()
    for j in case.split():
        if j == '@':
            total *= 3
        elif j == '%':
            total += 5
        elif j == '#':
            total -= 7
        else:
            total = float(j)
    print('%.2f'%total)

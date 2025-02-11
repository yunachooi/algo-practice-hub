count = 0

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break

    count += 1
    print(f'Triangle #{count}')

    if a == -1:
        if b >= c:
            print('Impossible.')
        else:
            a = (c ** 2 - b ** 2) ** (1/2)
            print('a = %.3f' % a)
            
    elif b == -1:
        if a >= c:
            print('Impossible.')
        else:
            b = (c ** 2 - a ** 2) ** (1/2)
            print('b = %.3f' % b)

    else:
        c = (a ** 2 + b ** 2) ** (1/2)
        print('c = %.3f' % c)

    print('')

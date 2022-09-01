n = int(input())

if n == 1:
    print('*')
else:
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

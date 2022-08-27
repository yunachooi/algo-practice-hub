n = int(input())
m = 2 * n - 1

for i in range(1, m + 1, 2):
    b = m - i
    print(' ' * int(b / 2) + '*' * i)

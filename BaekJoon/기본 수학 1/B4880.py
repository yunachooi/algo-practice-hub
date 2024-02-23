while True:
    x, y, z = map(int, input().split())
    if x == y == z :
        break
    else:
        if x + z == y * 2:
            print(f'AP {(2 * z) - y}')
        else:
            print(f'GP {(z ** 2) // y')

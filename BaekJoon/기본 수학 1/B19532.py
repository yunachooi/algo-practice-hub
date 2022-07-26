a, b, x, c, d, y = map(int, input().split())

for i in range(-999, 1000) :
    for j in range(-999, 1000) :
        if (a * i) + (b * j) == x and (c * i) + (d * j) == y :
            print(i, j)

n = int(input())
a, b = 1, 1

while True:
    if n <= a:
        print(b)
        break

    a += 6 * b
    b += 1

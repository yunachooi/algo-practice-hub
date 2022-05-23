n = int(input())
x = 2

while n != 1:
    if n % x == 0:
        n /= x
        print(x)
    else:
        x += 1

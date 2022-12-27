x = int(input())
L = 1

while x > L:
    x -= L
    L += 1

if L % 2 == 0:
    print(x, "/", L - x + 1, sep = '')
else:
    print(L - x + 1, "/", x, sep = '')

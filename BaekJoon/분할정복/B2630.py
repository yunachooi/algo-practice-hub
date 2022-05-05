n = int(input())
lst = []
white = blue = 0

for _ in range(n):
    lst.append(list(map(int, input().split())))

# start func
def result(x, y, n):
    global white, blue
    color = lst[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != lst[i][j]:
                result(x, y, n // 2)
                result(x, y + n // 2, n // 2)
                result(x + n // 2, y, n // 2)
                result(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
# end func

# main program
result(0, 0, n)
print(white)
print(blue)

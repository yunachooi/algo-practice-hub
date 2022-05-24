n = int(input())
num = 1

while True:
    n -= num
    if n >= 0:
        num += 1
    else:
        print(num - 1)
        break

lst = []

for i in range(1, 6):
    n = input()

    if 'FBI' in n:
        lst.append(i)


if lst:
    print(*lst)
else:
    print('HE GOT AWAY!')

cnt = 0

for _ in range(6):
    n = input()
    if n == 'W':
        cnt += 1

if cnt == 1 or cnt == 2:
    print('3')
elif cnt == 3 or cnt == 4:
    print('2')
elif cnt == 5 or cnt == 6:
    print('1')
else:
    print('-1')

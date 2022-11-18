N = int(input())

for i in range(1, N + 1):
    s = sum(1 for x in str(i) if x in ['3', '6', '9'])
    if s == 0:
        print(i, end = ' ')
    else:
        print('-'*s, end = ' ')

N = int(input())

for i in range(N):
    if N % (i + 1) == 0:
        print(i + 1, end = ' ')

a = [[0] * 15 for i in range(5)]

for i in range(5):
    w = list(input())
    w_len = len(w)

    for j in range(w_len):
        a[i][j] = w[j]

for i in range(15):
    for j in range(5):

        if a[j][i] == 0:
            continue;

        else:
            print(a[j][i], end='')

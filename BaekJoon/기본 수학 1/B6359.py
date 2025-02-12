for i in range(int(input())):
    n = int(input())
    cnt = 0

    for i in range(1, n):

        if i ** 2 <= n :
            cnt += 1
        else :
            break

    print(cnt)

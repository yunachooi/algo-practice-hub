lst = [i for i in range(1, 31)]

for i in range(28):
    N = int(input())
    lst.remove(N)

for i in lst:
    print(i)

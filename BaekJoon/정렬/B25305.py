n, k = map(int, input().split())
a = list(map(int,input().split()))

a = sorted(a, reverse = True)

print(a[k - 1])

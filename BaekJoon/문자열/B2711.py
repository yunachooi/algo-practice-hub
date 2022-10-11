t = int(input())

for _ in range(t):
    n, word = map(str, input().split())
    n = int(n)

    print(word[:n - 1], word[n:], sep='')

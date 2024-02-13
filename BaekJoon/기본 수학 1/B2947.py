n = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]
            print(" ".join(map(str, n)))

    if n == answer:
        break

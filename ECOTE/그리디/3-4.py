n, k = map(int, input().split())
result = 0

while True:
    # 나누어 떨어지는 수가 될 때까지 감소
    taget = (n // k) * k
    result += (n - taget)
    n = taget

    if n < k:
        break

    result += 1
    n //= k

#마지막 남은 수에 대해 1씩 감소
result += (n - 1)

print(result)

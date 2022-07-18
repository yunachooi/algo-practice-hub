n = int(input())
fib = [0, 1]

if n == 1 or n == 2:
    print('1')
else:
    for i in range(n - 1):
        fib.append(fib[i] + fib[i + 1])
    print(fib[-1])

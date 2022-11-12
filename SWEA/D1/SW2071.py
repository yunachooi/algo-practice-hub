T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    avg = round(sum(numbers) / len(numbers))
    print('#{} {}'.format(test_case, avg))

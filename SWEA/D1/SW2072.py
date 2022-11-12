T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    odd = [num for num in numbers if num % 2 == 1]
    print('#{} {}'.format(test_case, sum(odd)))

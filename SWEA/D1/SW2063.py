T = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
index = (T - 1) // 2

print('{}'.format(numbers[index]))

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 ~ n까지의 수 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# main #
a = int(input())

print('반복적으로 구현 : ', factorial_iterative(a))
print('재귀적으로 구현 : ', factorial_recursive(a))

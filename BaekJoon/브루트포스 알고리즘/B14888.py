import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

def plus(a, b):
    return a + b 
def minus(a, b):
    return a - b 
def mul(a, b):
    return a * b 
def div(a, b):
    if a < 0:
        return -(-a // b)
    return a // b

ops = [plus, minus, mul, div]
min_result = 1000000000
max_result = -1000000000
def dfs(idx, result):
    global min_result, max_result

    if idx == N:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            dfs(idx+1, ops[i](result, num[idx]))
            operators[i] += 1

dfs(1, num[0])
print(max_result)
print(min_result)

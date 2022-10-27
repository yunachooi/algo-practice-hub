import math

def solution(n):
    answer = 10
    while n < math.factorial(answer):
        answer -= 1
    return answer

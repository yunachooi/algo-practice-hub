def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i - 1] * b[i - 1]
    return answer

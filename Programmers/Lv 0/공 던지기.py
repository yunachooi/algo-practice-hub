def solution(numbers, k):
    answer = 0
    answer = numbers[2 * (k - 1) % len(numbers)]
    return answer

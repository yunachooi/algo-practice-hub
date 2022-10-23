def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.insert(i, numbers[i] * 2)
    return answer

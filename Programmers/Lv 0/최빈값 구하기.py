import statistics
def solution(array):
    answer = 0
    answer = statistics.multimode(array)
    if len(answer) >= 2:
        answer = -1
    else:
        answer = answer[0]
    return answer

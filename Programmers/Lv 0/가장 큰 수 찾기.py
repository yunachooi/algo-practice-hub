def solution(array):
    answer = []
    max = array[0]
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
    n = array.index(max)
    answer = [max, n]
    return answer

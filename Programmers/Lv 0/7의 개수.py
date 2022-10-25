def solution(array):
    answer = 0
    for i in range(len(array)):
        lst = str(array[i])
        for j in range(len(lst)):
            if lst[j] == '7':
                answer += 1
    return answer

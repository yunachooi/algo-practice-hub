def solution(order):
    answer = 0
    order = str(order)
    for i in range(len(order)):
        if order[i] == '3' or order[i] == '6' or order[i] == '9':
            answer += 1
    return answer

def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split('=')
        if eval(q[0]) == int(q[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer

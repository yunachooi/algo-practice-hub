def solution(s):
    answer = []
    for i in s.split(' '):
        if i == 'Z' and len(answer) > 0:
            answer.pop()
            continue
        answer.append(int(i))
    return sum(answer)

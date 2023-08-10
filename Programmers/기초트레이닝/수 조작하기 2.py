def solution(numLog):
    answer = ''


    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            answer += 'w'
        if numLog[i+1] - numLog[i] == -1:
            answer += 's'
        if numLog[i+1] - numLog[i] == 10:
            answer += 'd'
        if numLog[i+1] - numLog[i] == -10:
            answer += 'a'


    return answer

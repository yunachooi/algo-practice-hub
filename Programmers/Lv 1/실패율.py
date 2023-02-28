def solution(N, stages):
    answer = {}
    d = len(stages)
    
    for i in range(1, N + 1):
        if d != 0:
            cnt = stages.count(i)
            answer[i] = cnt / d
            d -= cnt
        else:
            answer[i] = 0
            
    return sorted(answer, key=lambda x : answer[x], reverse = True)

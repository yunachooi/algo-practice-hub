def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        tmp = []
        
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
                
        answer.append(-1 if not tmp else min(tmp))
        
    return answer

def solution(picture, k):
    answer = []
    
    for i in picture:
        mystr = ''
        
        for j in i:
            mystr += j*k
        for _ in range(k):
            answer.append(mystr)
            
    return answer

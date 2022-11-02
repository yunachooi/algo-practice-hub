def solution(score):
    answer = []
    lst = []
    for i in score:
        lst.append((i[0] + i[1]) / 2)
        
    lst.sort(reverse = True)
    
    for i in score:
        answer.append(lst.index((i[0] + i[1]) / 2) + 1)
    return answer

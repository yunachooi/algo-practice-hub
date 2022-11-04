def solution(lines):
    answer, lst = [], []
    for i in lines:
        for j in range(i[0], i[1]):
            if [j, j + 1] not in lst:                
                lst.append([j, j + 1])
            else:
                if [j, j + 1] not in answer:
                    answer.append([j, j + 1])
    return len(answer)

def solution(sizes):
    w, h = 0, 0
    for x in sizes:
        if x[0] < x[1]:
            x[1], x[0] = x[0], x[1]
    
    for x in sizes:
        if w < x[0]:    w = x[0]
        if h < x[1]:    h = x[1]
            
    return w * h

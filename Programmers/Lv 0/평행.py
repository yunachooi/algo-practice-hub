def solution(dots):
    lst = []
    for i in range(3):
        for j in range (i + 1, 4):
            x = dots[i][0] - dots[j][0]
            y = dots[i][1] - dots[j][1]
            
            k = y / x if x != 0 else -1
            if k not in lst:
                lst.append(k)
            else:   return 1
    return 0

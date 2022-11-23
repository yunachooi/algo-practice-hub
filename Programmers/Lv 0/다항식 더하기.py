def solution(polynomial):
    coef, const = 0, 0
    
    for i in polynomial.split(' + '):
        if 'x' in i:
            if len(i) != 1:
                coef += int(i[:-1]) - 1
            coef += 1 
        else:
            const += int(i)
            
    answer = []
    
    if coef != 0:
        answer.append('x' if coef == 1 else f'{coef}x')
    if const != 0:
        answer.append(str(const))
    return ' + '.join(answer) if answer else '0'

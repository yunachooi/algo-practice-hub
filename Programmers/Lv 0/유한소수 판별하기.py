import fractions

def solution(a, b):
    answer = []
    i = 2
    
    if a % b == 0:
        return 1
    
    fraction = fractions.Fraction(a, b)
    b = fraction.denominator
    
    # 소인수분해
    while b != 1:
        if b % i == 0:
            if i not in answer:
                answer.append(i)
            b /= i
        else:
            i += 1
    if answer == [2, 5] or answer == [2] or answer == [5]:
        answer = 1
    else:
        answer = 2
    return answer

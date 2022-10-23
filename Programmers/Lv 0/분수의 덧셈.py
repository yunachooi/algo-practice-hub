import math #gcd 사용

def solution(denum1, num1, denum2, num2):
    answer = []
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    
    gcd = math.gcd(denum, num)
    
    return [denum // gcd, num // gcd]

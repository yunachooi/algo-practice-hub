import math

def solution(n, m):
    gcd_n = math.gcd(n, m)
    lcm_n = n * m // math.gcd(n, m)
    
    return [gcd_n, lcm_n]

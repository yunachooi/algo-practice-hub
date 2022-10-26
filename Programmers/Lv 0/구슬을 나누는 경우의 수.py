import math
def solution(balls, share):
    answer = 0
    answer = math.factorial(balls) / (math.factorial((balls - share)) * math.factorial(share))
    return answer

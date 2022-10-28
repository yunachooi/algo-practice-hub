def solution(s):
    answer = ''
    answer = ''.join(sorted([i for i in s if s.count(i) == 1]))
    return answer

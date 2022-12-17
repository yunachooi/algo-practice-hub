def solution(s):
    answer = list(s)
    if s[0] == '-':
         answer = -int(s[1:])
    else:
        answer = int(s[0:])
    return answer

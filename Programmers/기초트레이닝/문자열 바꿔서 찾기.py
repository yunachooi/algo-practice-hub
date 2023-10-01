def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)

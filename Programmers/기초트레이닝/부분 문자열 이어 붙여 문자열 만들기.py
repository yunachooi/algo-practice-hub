def solution(my_strings, parts):
    return ''.join([i[j[0]:j[1]+1] for i, j in zip(my_strings, parts)])

def solution(my_string):
    answer = ''
    answer = ''.join(dict.fromkeys(my_string))
    return answer

def solution(my_string):
    answer = 0
    value = ''
    for i in my_string:
        if i.isdigit():
            value += i
        else:
            if value != '':
                answer += int(value)
                value = ''
    if value != '':
        answer += int(value)
    return answer

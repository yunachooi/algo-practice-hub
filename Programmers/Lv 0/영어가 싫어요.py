def solution(numbers):
    answer = ''
    start, end = 0, 0
    lst = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4',
           'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    while end < len(numbers):
        end += 1
        if numbers[start : end] in lst:
            answer += lst[numbers[start : end]]
            start = end
    return int(answer)

def solution(my_string):
    answer = 0
    for i in my_string :
        if i.isdigit() :
            i = int(i)
            answer += i
    return answer

def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    position = array.index(n)
    
    if len(array) == position + 1:
        answer = array[position - 1]
    elif array[position - 1] == array[position + 1]:
        answer = array[position + 1]
    elif abs(array[position - 1] - n) > array[position + 1] - n:
        answer = array[position + 1]
    else:
        answer = array[position - 1]
    return answer

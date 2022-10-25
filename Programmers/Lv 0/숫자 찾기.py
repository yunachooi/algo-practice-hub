def solution(num, k):
    answer = -1
    num = str(num)
    k = str(k)
    for i in range(len(num)):
        if num[i] in k:
            return i + 1
    return answer

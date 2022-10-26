def solution(A, B):
    answer = -1
    for i in range(len(A)):
        if A == B :
            return i
        else :
            A = A[-1]+A[0:-1]
    return answer

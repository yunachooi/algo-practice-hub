def solution(n):
    answer = set(range(2, n + 1))
    
    for i in range(2, n // 2 + 2):
        if i in answer:
            answer -= set(range(2 * i, n + 1, i))

    return len(answer)

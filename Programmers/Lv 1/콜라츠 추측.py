def solution(num):
    cnt = 0

    while num != 1 and cnt < 500:
        num = 3 * num + 1 if num % 2 else num // 2
        cnt += 1
        
    return cnt if cnt < 500 else -1

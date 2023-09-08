def solution(numbers, n):
    sum = 0
    
    for elem in numbers:
        if sum > n:
            return sum
        
        else:
            sum += elem
            
    return sum

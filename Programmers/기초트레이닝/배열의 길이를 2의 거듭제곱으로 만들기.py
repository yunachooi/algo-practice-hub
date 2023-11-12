def solution(arr):
    num = 1
    
    while num < len(arr):
        num *= 2
    while num != len(arr):
        arr.append(0)
        
    return arr

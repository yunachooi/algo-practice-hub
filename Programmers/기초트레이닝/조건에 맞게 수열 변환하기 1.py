def solution(arr):
    for i in range(len(arr)):
        x = arr[i]
        
        if x >= 50 and not x % 2 :
            arr[i] //= 2
        elif x < 50 and x % 2 :
            arr[i] *= 2
            
    return arr

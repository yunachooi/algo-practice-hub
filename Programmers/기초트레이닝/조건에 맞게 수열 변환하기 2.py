def solution(arr):
    answer = 0
    mylist = []
    
    while mylist != arr:
        answer += 1
        mylist = arr[::]
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
                
    return answer - 1

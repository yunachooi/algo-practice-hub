def solution(arr1, arr2):
        if sum(arr1) == sum(arr2):
            return 0
        
        else:
            if sum(arr1) > sum(arr2):
                return 1
            
            elif sum(arr1) < sum(arr2):
                return -1

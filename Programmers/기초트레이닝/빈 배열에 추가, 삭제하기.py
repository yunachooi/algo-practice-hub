def solution(arr, flag):
    arr1 = []
    
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1

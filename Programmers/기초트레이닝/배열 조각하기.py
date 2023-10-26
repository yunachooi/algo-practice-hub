def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr

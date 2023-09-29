def solution(arr, queries):
    for (s, e) in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr

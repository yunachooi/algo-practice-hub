def solution(arr, queries):
    for i in queries:
        for j in range(i[0], i[1] + 1):
            if j / i[2] == j // i[2]:
                arr[j] += 1
    return arr

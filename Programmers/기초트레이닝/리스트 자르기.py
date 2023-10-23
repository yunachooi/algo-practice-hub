def solution(n, slicer, num_list):
    a, b, c = slicer
    b += 1
    if n == 1:
        return num_list[0 : b]
    if n == 2:
        return num_list[a :]
    if n == 3:
        return num_list[a : b]
    if n == 4:
        return num_list[a : b : c]

def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    return d[(sum(m[:a - 1]) + b - 1) % 7]

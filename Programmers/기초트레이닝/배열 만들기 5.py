def solution(intStrs, k, s, l):
    return [int(j) for j in [i[s : s + l] for i in intStrs] if int(j) > k]

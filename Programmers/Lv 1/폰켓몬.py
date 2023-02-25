def solution(nums):
    answer = 0
    n = len(nums) // 2
    lst = set(nums)
    # set - 중복되지 않은 원소만 얻음
    
    if n >= len(lst):
        return len(lst)
    else:   return n

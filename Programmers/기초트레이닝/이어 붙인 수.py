def solution(num_list):
    even = int(''.join([str(i) for i in num_list if i % 2 == 0]))
    odd = int(''.join([str(i) for i in num_list if not i % 2 == 0]))
    
    return even + odd

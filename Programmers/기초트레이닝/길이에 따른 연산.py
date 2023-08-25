def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    
    else:
        return eval('*'.join(list(map(str, num_list))))

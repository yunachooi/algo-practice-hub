def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        lst = str(bin(a1 | a2))[2:]
        
        lst = lst.rjust(n, '0')
        # rjust = 0을 제외한 다른 문자로 채우기
        
        lst = lst.replace('1', '#')
        lst = lst.replace('0', ' ')
        
        answer.append(lst)
    return answer

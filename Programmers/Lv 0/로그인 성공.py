def solution(id_pw, db):
    answer = 'fail'
    lst = []
    
    for i in range(len(db)):
        lst.append(db[i][0])
        
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in lst:
        answer = 'wrong pw'
        
    return answer

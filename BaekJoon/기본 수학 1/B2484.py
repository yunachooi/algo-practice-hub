n = int(input())
result = []

for _ in range(n) :
    dices = list(map(int,input().split()))
    set_dices = list(set(dices))
    tmp = []
    
    for i in set_dices :
        tmp.append(dices.count(i))

    if len(set_dices) == 1 :
        result.append(50000 + set_dices[0]*5000)
    
    elif len(set_dices) == 2 :
        if len(tmp) == 2 :
            if tmp[0] != tmp[1] :
                result.append(10000 + set_dices[tmp.index(max(tmp))] * 1000)
            else :
                result.append(2000 + set_dices[0] * 500 + set_dices[1] * 500)
    
    elif len(set_dices) == 3 :
        result.append(1000 + set_dices[tmp.index(max(tmp))] * 100)
    
    elif len(set_dices) == 4:
        result.append(max(dices) * 100)
    
print(max(result))

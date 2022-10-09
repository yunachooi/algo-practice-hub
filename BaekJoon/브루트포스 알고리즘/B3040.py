lst = []
t = 0

for _ in range(9):
    r = int(input())
    lst.append(r)
    t += r
    
for i in range(9):
    for j in range(i + 1, 9):
        if t - lst[i] - lst[j] == 100:
            n1, n2 = lst[i], lst[j] 
            lst.remove(n1)
            lst.remove(n2)
            
            for i in lst:
                print(i)
            break
     
    if len(lst) < 9:
        break

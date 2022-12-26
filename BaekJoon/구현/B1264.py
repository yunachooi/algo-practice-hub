lst = ['a','e','i','o','u']


while True:
    cnt = 0
    n = list(input().lower())
    
    if n[0] == '#':
        break
   
    for i in n:
        if i in lst:
            cnt += 1
    print(cnt)

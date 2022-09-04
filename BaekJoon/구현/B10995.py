n = int(input())

if n == 1:
    print('*')
    
else:
    for i in range(n):
        if i % 2:
            print(' *' * n)
            
        else:
            print('* ' * n)

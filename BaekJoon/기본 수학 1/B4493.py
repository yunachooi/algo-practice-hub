n = int(input())
 
for i in range(n) :
    m = int(input())
    p1 = 0
    p2 = 0
    
    for j in range(m) :
       x, y = input().split()
    
       if x == y :
          continue
       elif (x == 'S' and y == 'P') or (x=='R' and y== 'S') or (x == 'P' and y == 'R') :
          p1 = p1 + 1
       else :
          p2 = p2 + 1
            
    if p1 == p2 :
       print('TIE')
    elif p1 > p2 :
       print('Player 1')
    else :
       print('Player 2')

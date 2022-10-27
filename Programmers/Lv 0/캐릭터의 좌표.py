def solution(keyinput, board):
    lst = {'up' : (0, 1) , 'down' : (0, -1), 'left' : (-1, 0) , 'right' : (1, 0)}
    x, y = 0, 0
    
    for i in keyinput:
        dx = x + lst[i][0]
        dy = y + lst[i][1]
        
        if abs(dx) > board[0] // 2 or abs(dy) > board[1] // 2:
            continue
        else:
            x = dx
            y = dy
            
    answer = [x, y]
    return answer

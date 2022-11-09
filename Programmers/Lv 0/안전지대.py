def solution(board):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1),
           (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for dx, dy in move:
                    x, y = i + dx, j + dy
                    
                    if x not in range(len(board)):
                        continue
                    if y not in range(len(board)):
                        continue
                    if board[x][y] == 1:
                        continue
                    board[x][y] = -1
                    
    return sum([1 for i in range(len(board)) for j in range(len(board)) if board[i][j] == 0])

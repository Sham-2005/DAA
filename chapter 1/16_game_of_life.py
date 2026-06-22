def gameOfLife(board):
    import copy
    m, n = len(board), len(board[0])
    copy_board = copy.deepcopy(board)
    
    for r in range(m):
        for c in range(n):
            live_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0: continue
                    nr, nc = r + i, c + j
                    if 0 <= nr < m and 0 <= nc < n and copy_board[nr][nc] == 1:
                        live_neighbors += 1
            
            if copy_board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 0
            else:
                if live_neighbors == 3:
                    board[r][c] = 1
    return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
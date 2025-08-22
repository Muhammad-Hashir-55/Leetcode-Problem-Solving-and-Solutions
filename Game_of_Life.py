class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        eight_n = [(0,1),(1,0),(-1,0),(0,-1), (1,1),(1,-1),(-1,1),(-1,-1)]
        def count_neighbors(row,col):
            coun = 0
            for r,c in eight_n:
                n_r = row + r
                n_c = col + c
                
                if(0 <= n_r < m and 0 <= n_c < n):
                    if(board[n_r][n_c] in [1,-1]):
                        coun +=1
            return coun
        
        for i in range(m):
            for j in range(n):
                tot = count_neighbors(i,j)
                if(tot < 2 and board[i][j] ==1):
                    board[i][j] = -1
                elif((tot == 3 or tot == 2) and board[i][j] == 1):
                    continue
                elif(board[i][j] == 1 and tot > 3):
                    board[i][j] = -1
                elif(board[i][j] == 0 and tot ==3):
                    board[i][j] =2
        for i in range(m):
            for j in range(n):
                if(board[i][j] == -1):
                    board[i][j] = 0
                elif(board[i][j] == 2):
                    board[i][j] = 1
        

        

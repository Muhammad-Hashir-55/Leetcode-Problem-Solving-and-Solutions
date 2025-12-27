class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            r_c =[]
            for j in i:
                if(j != '.'):
                    r_c.append(j)
            if(len(r_c) != len(set(r_c))):
                return False
        
        
        for i in range(9):
            c_c = []
            for j in range(9):
                if(board[j][i] != '.'):
                    c_c.append(board[j][i])
            if(len(c_c) != len(set(c_c))):
                return False
        
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                b_c = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if(board[k][l] != '.'):
                            b_c.append(board[k][l])
                if(len(b_c) != len(set(b_c))):
                    return False
        return True

        

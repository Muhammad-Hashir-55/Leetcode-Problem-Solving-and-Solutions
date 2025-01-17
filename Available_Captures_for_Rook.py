class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        position = []
        n = len(board)
        for i in range(n):
            for j in range(n):
                if(board[i][j]=='R'):
                    position = [i,j]
        x1 = position[0]
        x2 = position[1]
        c= 0
        while(x1>=0):
            if(board[x1][x2]=='B'):
                break
            elif(board[x1][x2]=='p'):
                c +=1
                break
            x1 -=1
        x1 = position[0]
        x2 = position[1]
        
        while(x1<n):
            if(board[x1][x2]=='B'):
                break
            elif(board[x1][x2]=='p'):
                c +=1
                break
            x1 +=1
        
        x1 = position[0]
        x2 = position[1]
        
        while(x2>=0):
            if(board[x1][x2]=='B'):
                break
            elif(board[x1][x2]=='p'):
                c +=1
                break
            x2 -=1
        

        x1 = position[0]
        x2 = position[1]
        
        while(x2<n):
            if(board[x1][x2]=='B'):
                break
            elif(board[x1][x2]=='p'):
                c +=1
                break
            x2 +=1
        return c
        

        
        


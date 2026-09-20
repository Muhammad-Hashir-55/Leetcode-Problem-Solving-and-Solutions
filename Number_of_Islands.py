class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def trav(i,j,n,m):
            if(i<0 or j < 0 or i ==n or j == m or grid[i][j] == '0'):
                return
            grid[i][j] = '0'

            trav(i+1,j,n,m)
            trav(i,j+1,n,m)
            trav(i-1,j,n,m)
            trav(i,j-1,n,m)
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == '1'):
                    count +=1
                    trav(i,j,n,m)
        return count

        

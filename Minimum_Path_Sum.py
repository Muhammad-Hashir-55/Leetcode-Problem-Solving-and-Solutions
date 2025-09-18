class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = []
        for i in range(n):
            dp.append([0]*m)
        
        dp[0][0] = grid[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,m):
            dp[0][j] =  dp[0][j-1] + grid[0][j]
        
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]= grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        
        return dp[n-1][m-1]
        

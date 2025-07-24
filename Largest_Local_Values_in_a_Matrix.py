class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        bg = []
        n = len(grid)
        m = n
        for i in range(1,n-1):
            arr = []
            x = []
            for j in range(1,m-1):
                arr.append(grid[i-1][j-1])
                arr.append(grid[i-1][j])
                arr.append(grid[i-1][j+1])
                arr.append(grid[i][j-1])
                arr.append(grid[i][j])
                arr.append(grid[i][j+1])
                arr.append(grid[i+1][j-1])
                arr.append(grid[i+1][j])
                arr.append(grid[i+1][j+1])
                x.append(max(arr))
                arr = []
            bg.append(x)
        return bg
        

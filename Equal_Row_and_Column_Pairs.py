class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:


        n = len(grid)
        t_grid = []
        for i in range(n):
            x = []
            for j in range(n):
                x.append(grid[j][i])
            t_grid.append(x)
        

        tot = 0


        for i in range(n):
            for j in range(n):
                if(grid[i] == t_grid[j]):
                    tot +=1
        return tot


        

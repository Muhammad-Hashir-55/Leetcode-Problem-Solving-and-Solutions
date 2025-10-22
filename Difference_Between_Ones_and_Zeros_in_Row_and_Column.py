class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ones_r = []
        for i in range(n):
            ones_r.append(sum(grid[i]))
        

        ones_c = []
        for j in range(m):
            s= 0
            for i in range(n):
                s += grid[i][j]
            ones_c.append(s)
        


        diff = []
        base = -(m+n)
        for i in range(n):
            x = []
            for j in range(m):
                res = 2 * ones_r[i] + 2 * ones_c[j] + base
                x.append(res)
            diff.append(x)
        return diff




        

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        a = []
        rep = -1
        
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if(grid[i][j] in s):
                    rep = grid[i][j]
                else:
                    s.add(grid[i][j])
                    a.append(grid[i][j])
    
        elem = 1
        a.sort()
        print(a)
        for i in a:
            if(i != elem):
                break
            elem +=1
        return [rep , elem]

        

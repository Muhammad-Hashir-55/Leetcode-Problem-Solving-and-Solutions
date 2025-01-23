class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        c = 0
        check = []
        
        cc = False
        while(cc != True):
            arr = []
            print(grid)
            for i in grid:
                if(not i):
                    cc = True
                    break
                maxi = max(i)
                arr.append(maxi)
                i.remove(maxi)
            if(arr):
                c += max(arr)
                
        return c
        

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n= len(grid)
        
        for i in range(n):
            for j in range(1):
                k = i
                l = j
                arr = []
                while(k < n and l < n):
                    arr.append(grid[k][l])
                    k +=1
                    l +=1
                arr.sort(reverse=True)

                k = i
                l = j
                idx = 0
                while(k < n and l < n):
                    grid[k][l] = arr[idx]
                    idx +=1
                    k +=1
                    l +=1
                    
        for i in range(1):
            for j in range(1,n):
                k = i
                l = j
                arr = []
                while(k < n and l < n):
                    arr.append(grid[k][l])
                    k +=1
                    l +=1
                arr.sort()

                k = i
                l = j
                idx = 0
                while(k < n and l < n):
                    grid[k][l] = arr[idx]
                    idx +=1
                    k +=1
                    l +=1

        return grid
                    

        

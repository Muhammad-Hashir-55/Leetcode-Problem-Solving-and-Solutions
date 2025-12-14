class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []
        for i in range(m):
            x = []
            for j in range(n):
                x.append(0)
            matrix.append(x)
        for i in indices:
            for j in range(0,n):
                matrix[i[0]][j] +=1
            for j in range(0,m):
                matrix[j][i[1]] +=1
        count = 0
        for i in matrix:
            for j in i:
                if(j%2 !=0):
                    count +=1
        return count

        

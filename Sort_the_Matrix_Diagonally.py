class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                k = i
                l = j
                arr = []
                while(k<n and l < m ):
                    arr.append(mat[k][l])
                    k +=1
                    l +=1
                arr.sort()
                
                k = i
                l = j
                idx = 0
                while(k < n and l < m):
                    mat[k][l]= arr[idx]
                    idx +=1
                    k +=1
                    l +=1
                


        return mat


        

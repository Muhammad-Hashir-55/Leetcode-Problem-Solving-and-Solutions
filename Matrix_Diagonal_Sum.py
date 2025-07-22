class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumi = 0
        n = len(mat)
        if(n % 2 == 0):
            for i in range(n):
                sumi += mat[i][i]
            idx= n-1
            for i in range(n):
                sumi += mat[i][idx]
                idx -=1
            return sumi
        elif(n ==1):
            return mat[0][0]
        else:
            for i in range(n):
                sumi += mat[i][i]
            idx= n-1
            for i in range(n):
                sumi += mat[i][idx]
                idx -=1
            sumi = sumi - mat[n//2][n//2]
            return sumi


        
        

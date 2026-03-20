import numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr = np.array(matrix)
        
        n = len(matrix)
        for i in range(n):
            idxes = []
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    idxes.append(j)
            for j in idxes:
                arr[i] = 0
                arr[:,j] = 0
        for i in range(n):
            l = []
            for j in arr[i]:
                l.append(int(j))
            matrix[i] = l
        return matrix

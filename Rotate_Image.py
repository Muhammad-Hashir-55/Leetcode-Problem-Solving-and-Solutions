class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # using vertical transpose
        top = 0
        n =len(matrix)
        bottom = n -1
        while(top < bottom):
            for col in range(n):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top +=1
            bottom -=1
        
        # now taking transpose
        for i in range(n):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix
        

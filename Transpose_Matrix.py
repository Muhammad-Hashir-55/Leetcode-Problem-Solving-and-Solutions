class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        m = len(matrix)
        trans = [0]*n
        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrix[j][i])
            trans[i] = row
        
        return trans

        

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        store = []
        for i in range(m):
            x = []
            for j in range(n):
                x.append(matrix[j][i])
            store.append(x)
        print(store)
        bg = []
        for i in range(n):
            x = []
            for j in range(m):
                if(matrix[i][j] == -1):
                    x.append(max(store[j]))
                else:
                    x.append(matrix[i][j])
            bg.append(x)
        return bg
                
        

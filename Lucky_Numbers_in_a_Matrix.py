class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        omat = []
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        for i in range(m):
            x = []
            for j in range(n):
                x.append(matrix[j][i])
            omat.append(x)
        for i in matrix:
            mini = min(i)
            for j in i:
                if(j == mini):
                    for k in omat:
                        maxi = max(k)
                        if(j == mini and j == maxi):
                            ans.append(j)
                            continue
                else:
                    continue
                
        return ans


        

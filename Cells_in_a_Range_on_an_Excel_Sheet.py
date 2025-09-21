class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        x = s.split(':')
        alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        arr = []
        for i in range(alphas.index(x[0][0]) , alphas.index(x[1][0]) +1):
            for j in range(int(x[0][1]) , int(x[1][1]) + 1):
                arr.append(alphas[i]+ str(j))
        return arr
            
            
        

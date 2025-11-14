class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        bg = []
        for i in range(n+1):
            bg.append([0]* (n+1))
        for i in queries:
            r1,c1,r2,c2 = i
            bg[r1][c1] +=1
            bg[r1][c2+1] -=1
            bg[r2+1][c1] -=1
            bg[r2+1][c2+1] +=1
        
        for i in range(n):
            for j in range(1,n):
                bg[i][j] += bg[i][j-1]

        for j in range(n):
            for i in range(1,n):
                bg[i][j] += bg[i-1][j]
        
        fin = []
        for i in range(n):
            x = []
            for j in range(n):
                x.append(bg[i][j])
            fin.append(x)
        return fin
        

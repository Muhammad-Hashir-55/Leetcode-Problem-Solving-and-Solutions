class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1 or numRows >= len(s)):
            return s
        idx = 0
        d = 0 # direction
        rows = [[] for _ in range(numRows)]


        for c in s:
            rows[idx].append(c)
            if(idx == 0):
                d = 1
            elif(idx == numRows -1):
                d = -1
            idx +=d
        
        res = ''
        for i in rows:
            for j in i:
                res += j
        return res


        

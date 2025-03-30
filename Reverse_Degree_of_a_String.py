class Solution:
    def reverseDegree(self, s: str) -> int:
        ss = 'abcdefghijklmnopqrstuvwxyz'
        ss = ss[::-1]
        ss = '0' + ss
        prd = 0
        n = len(s)
        for i in range(n):
            idx = i + 1
            rev_idx = ss.index(s[i])
            prd  = prd + (idx * rev_idx)
        return prd

        

class Solution:
    def countAsterisks(self, s: str) -> int:
        idxs = []
        n = len(s)
        tot=0
        if('|'not in s):
            return s.count('*')
        idx = s.index('|')
        tot += s[:idx].count("*")

        for i in range(n):
            if(s[i] == '|'):
                idxs.append(i)

        
        n = len(idxs)
        for i in range(1,n-1,2):
            ss = s[idxs[i]:idxs[i+1]]
            tot += ss.count('*')
        
        tot += s[idxs[-1]:].count('*')
        return tot

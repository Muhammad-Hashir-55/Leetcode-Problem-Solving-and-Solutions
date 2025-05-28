class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def count(s,l,r):
            coun =0
            while(l >=0 and r < len(s) and s[l] == s[r]):
                coun +=1
                l -=1
                r +=1
            return coun
        tot = 0
        for i in range(n):
            tot += count(s,i,i)
            tot += count(s,  i , i+1)
        return tot

        

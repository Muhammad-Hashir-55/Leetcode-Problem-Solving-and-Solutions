class Solution:
    def numSub(self, s: str) -> int:
        # nice
        n = len(s)
        res = 0
        nn = 0
        
        for i in range(n):
            if(s[i] == '1'):
                nn +=1
                continue
            else:
                res += (nn * (nn+1))//2
                nn = 0
        res += (nn * (nn+1))//2

        return res % (10**9 + 7)


        

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        tot = (n * (n+1))//2
        coun = 0
        for i in range(n):
            x = s[i]
            for j in range(i+1,n):
                x += s[j]

                coun0 = x.count('0')
                coun1 = x.count('1')
                if(coun1 > k and coun0 > k):
                    
                    coun +=1
        return tot - coun

        

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        s = s[2:]
        n =len(s)
        for i in range(n-1):
            if(s[i]!= s[i+1]):
                continue
            else:
                return False
        return True
        

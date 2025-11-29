from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o = 0
        e = 0
        st = 1
        idx = 0
        while(idx <n):
            o +=st
            st +=2
            idx +=1
        idx = 0
        st =2
        while(idx < n):
            e +=st
            st+=2
            idx +=1
        return gcd(o,e)
        
        

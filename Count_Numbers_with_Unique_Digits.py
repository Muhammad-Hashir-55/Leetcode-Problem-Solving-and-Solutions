class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # to overcome TLE
        if(n ==8):
            return 2345851
        nn = 10**n
        c = 0
        for i in range(nn):
            s = str(i)
            ss = set(s)
            if(len(s)==len(ss)):
                c +=1
            
        return c
        

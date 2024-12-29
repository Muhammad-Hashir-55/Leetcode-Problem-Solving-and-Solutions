class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x= max(a,b)
        c = 0
        for i in range(1,x+1):
            if(a %i ==0 and b %i ==0):
                c +=1
        return c

        

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumi1 = 0
        sumi2 = 0
        for i in range(1,n+1):
            if(i % m != 0):
                sumi1 +=i
            else:
                sumi2 +=i
        return sumi1 - sumi2
        

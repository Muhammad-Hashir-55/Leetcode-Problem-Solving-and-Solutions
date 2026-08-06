class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while(True):
            s = str(n)
            x = 1
            for i in s:
                x *= int(i)
            if(x%t == 0):
                return n
            n +=1
        

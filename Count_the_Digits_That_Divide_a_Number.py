class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        c = 0
        for i in s:
            if(num % int(i)==0):
                c +=1
        return c
        

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        sumi = 0
        for i in s:
            sumi +=int(i)
        if(x % sumi == 0):
            return sumi
        else:
            return -1
        

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        sumi = 0
        c = True
        for i in s:
            if(c == True):
                sumi +=int(i)
                c = False
            else:
                sumi -=int(i)
                c = True
        return sumi
        

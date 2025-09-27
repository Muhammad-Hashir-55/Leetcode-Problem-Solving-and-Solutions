class Solution:
    def clearDigits(self, s: str) -> str:
        digits = '0123456789'
        s = list(s)
        while(True):
            c = False
            for i in range(1,len(s)):
                if(s[i] in digits and s[i-1] not in digits ):
                    s.pop(i)
                    s.pop(i-1)
                    c= True
                    break
            if(c == False):
                break
        return ('').join(s)

        

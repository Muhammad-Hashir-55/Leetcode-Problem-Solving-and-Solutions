class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            ss = ''
            n = len(s)
            for i in range(1,n):
                sumi = int(s[i-1]) + int(s[i])
                ss += str(sumi % 10)
            s = ss
        if(len(set(s)) == 1):
            return True
        else:
            return False
        

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if(len(s)<4):
            return s
        else:
            c = 1
            nn = len(s)
            for i in range(nn-1,-1,-1):
                if(c %3 ==0 and i !=0):
                    s = s[:i] +"."+s[i:]
                c +=1
        return s

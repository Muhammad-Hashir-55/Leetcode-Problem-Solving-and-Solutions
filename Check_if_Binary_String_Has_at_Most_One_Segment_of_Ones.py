class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if(s.count('1')==1):
            return True
        n= len(s)
        for i in range(1,n-1):
            if(s[i]=='0' and s[i+1]=='1'):
                return False
        return True
            

        

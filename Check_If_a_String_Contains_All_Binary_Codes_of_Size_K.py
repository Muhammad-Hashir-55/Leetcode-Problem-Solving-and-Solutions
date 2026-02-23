class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        ss = set()
        real = 2**k
        n= len(s)
        
        for i in range(0,n-k +1):
            test = s[i:i+k]
            ss.add(test)
            if(len(ss) == real):
                return True
        return False


        

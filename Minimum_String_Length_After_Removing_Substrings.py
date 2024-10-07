
class Solution:
    def minLength(self, s: str) -> int:
        while(True):
            n = len(s)
            if("AB" in s):
                i = s.index("AB")
                s = s[:i] + s[i+2:]
            if("CD" in s):
                i = s.index("CD")
                s = s[:i] + s[i+2:]
            if(n == len(s)):
                break
        return len(s)
            

        
check = Solution()
print(check.minLength("ACBBD"))

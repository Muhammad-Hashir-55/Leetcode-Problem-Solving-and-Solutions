class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while("()" in s):
            ii = s.index("()")
            s = s[:ii] + s[ii+2:]
        return len(s)
        

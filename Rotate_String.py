class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if(n ==0):
            return False
        for i in range(n):
            s = s[-1] + s
            s = s[:-1]
            if(s ==goal):
                return True
        return False
        

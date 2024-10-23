class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n = len(s)
        for i in range(n-1):
            if(s.count(s[i])!= s.count(s[i+1])):
                return False
        return True
        

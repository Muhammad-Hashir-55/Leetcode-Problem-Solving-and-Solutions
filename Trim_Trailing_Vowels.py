class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        while(s[-1] in 'aeiou'):
            s = s[:-1]
            if(not s):
                break
        return s
        

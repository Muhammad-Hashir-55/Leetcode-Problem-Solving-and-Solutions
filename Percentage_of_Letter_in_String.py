class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        x = s.count(letter)
        aa = (x/n)*100
        return int(aa)
        

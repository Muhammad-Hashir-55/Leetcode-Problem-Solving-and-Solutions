class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)

        sumi = 0
        for i in range(n):
            j = t.index(s[i])
            sumi += abs(i -j)
        return sumi
        

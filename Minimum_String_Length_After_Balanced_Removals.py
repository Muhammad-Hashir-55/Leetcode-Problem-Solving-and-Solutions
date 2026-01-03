class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        n = len(s)
        c1 = s.count('a')
        c2 = s.count('b')
        mini = min(c1,c2)
        return n - 2*mini
        


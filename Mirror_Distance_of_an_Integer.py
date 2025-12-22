class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        s = s[::-1]
        nn = int(s)
        return abs(n- nn)
        

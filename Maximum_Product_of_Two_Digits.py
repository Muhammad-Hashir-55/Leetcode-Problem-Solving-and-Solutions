class Solution:
    def maxProduct(self, n: int) -> int:
        s= str(n)
        k = sorted(s)
        return int(k[-1]) * int(k[-2])
        

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ms = ''
        for i in range(1,n+1):
            s = bin(i)[2:]
            ms +=s
        return int(ms,2) % (10**9 + 7)
        

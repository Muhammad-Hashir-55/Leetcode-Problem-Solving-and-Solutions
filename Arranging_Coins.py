class Solution:
    def arrangeCoins(self, n: int) -> int:
        x =0
        while(n >=0):
            x +=1
            n -=x
        return x-1
        

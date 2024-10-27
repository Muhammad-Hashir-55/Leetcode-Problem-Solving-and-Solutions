class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = -121212
        while(n != original):
            n = original
            for i in nums:
                if(i ==original):
                    original  = original *2
        return original
        

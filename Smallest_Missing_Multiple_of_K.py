class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        x = k
        while(True):
            if(x not in s):
                return x
            x +=k
        

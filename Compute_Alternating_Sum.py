class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sumi = 0
        n = len(nums)
        for i in range(n):
            if(i % 2 == 0):
                sumi += nums[i]
            else:
                sumi -= nums[i]
        return sumi
        

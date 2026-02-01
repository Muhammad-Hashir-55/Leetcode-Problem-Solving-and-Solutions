class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sumi = nums[0]
        nums = nums[1:]
        nums.sort()
        for i in range(2):
            sumi += nums[i]
        return sumi
        
        

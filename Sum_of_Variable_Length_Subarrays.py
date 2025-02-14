class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        sumi = 0
        for i in range(n):
            start = max(0,i - nums[i])
            a = nums[start:i+1]
            sumi = sumi + sum(a)
        return sumi

        

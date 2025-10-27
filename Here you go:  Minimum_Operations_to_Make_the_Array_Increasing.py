class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        n = len(nums)
        for i in range(1,n):
            if(nums[i]<= nums[i-1]):
                diff = nums[i-1] - nums[i]
                diff +=1
                nums[i] += diff
                ops +=diff

        return ops

        

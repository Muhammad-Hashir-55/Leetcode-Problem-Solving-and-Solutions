class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        n = len(nums)
        for i in range(1,n):
            if(nums[i]<mini):
                mini = nums[i]
        return mini
        

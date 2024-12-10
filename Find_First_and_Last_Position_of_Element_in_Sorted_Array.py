class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            return [-1,-1]
        x1 = nums.index(target)
        n = len(nums)
        x2 = -1
        for i in range(n-1,-1,-1):
            if(nums[i]== target):
                x2 = i
                break
        return [x1,x2]
        

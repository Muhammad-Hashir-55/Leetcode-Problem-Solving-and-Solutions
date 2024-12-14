class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<2):
            return 0
        nums.sort()
        maxi = -999999988
        for i in range(1,n):
            if(maxi < nums[i]-nums[i-1]):
                maxi = nums[i] - nums[i-1]
        return maxi

        

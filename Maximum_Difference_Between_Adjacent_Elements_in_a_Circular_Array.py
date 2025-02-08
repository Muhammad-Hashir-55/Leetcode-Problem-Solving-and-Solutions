class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        n = len(nums)
        maxi = -1
        for i in range(n-1):
            x = abs(nums[i]- nums[i+1])
            if(x>maxi):
                maxi = x
        return maxi

        

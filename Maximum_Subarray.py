class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadane's algorithm
        maxi = -99999999999999999999999999999999
        current = 0
        n = len(nums)
        for i in range(n):
            current +=nums[i]
            maxi = max(current,maxi)
            if(current <0):
                current = 0
        
            
        return maxi

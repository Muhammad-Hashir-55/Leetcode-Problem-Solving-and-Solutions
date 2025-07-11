class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # my Solution
        sumi = sum(nums)
        f = 0
        n = len(nums)
        for i in range(n):
            f += i * nums[i]
        
        maxi = f
        for i in range(1,n):
            f = f + sumi - n * nums[-i]
            maxi = max(maxi , f)
        return maxi 
        

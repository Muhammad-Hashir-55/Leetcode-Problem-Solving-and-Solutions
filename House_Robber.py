class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        
        prev1 , prev2 = 0,0
        for i in nums:
            prev1 , prev2 = max(prev1 , prev2 + i) , prev1
            
        
        return prev1

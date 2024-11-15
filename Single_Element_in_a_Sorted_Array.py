class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums[1:]:
            ans = ans^i
        return ans
        

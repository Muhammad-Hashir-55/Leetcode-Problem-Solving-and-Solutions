class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            sm = min(nums)
            idx = nums.index(sm)
            nums[idx] = nums[idx] * multiplier
        return nums
        

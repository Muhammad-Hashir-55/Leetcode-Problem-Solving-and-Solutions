class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if(sum(nums) % k == 0):
            return 0
        x = sum(nums)
        ops = 0
        while(sum(nums) % k != 0):
            maxi = max(nums)
            idx = nums.index(maxi)
            maxi -= 1
            nums[idx] = maxi
            ops +=1
        return ops
        

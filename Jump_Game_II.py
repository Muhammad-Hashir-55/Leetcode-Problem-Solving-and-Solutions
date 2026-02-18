class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        far = 0
        jumps = 0
        n = len(nums)
        while(far < n-1):
            farthest = 0
            for i in range(near , far +1):
                farthest = max(farthest , i + nums[i])
            near = far +1
            far = farthest
            jumps +=1
        return jumps
        

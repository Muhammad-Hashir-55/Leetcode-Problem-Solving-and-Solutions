class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        import math
        mini = math.inf
        for i in range(n):
            sumi = 0
            
            for j in range(i,n):
                sumi += nums[j]
                if(sumi >= target):
                    mini = min(mini , j-i +1)
                    break
                
        if(mini == math.inf):
            return 0
        else:
            return mini

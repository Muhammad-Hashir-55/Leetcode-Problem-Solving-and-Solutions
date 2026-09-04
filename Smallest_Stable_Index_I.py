class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            x1 = nums[:i+1]
            x2 = nums[i:]
            maxi = max(x1)
            mini = min(x2)
            if(maxi - mini <=k):
                return i
        return -1
        

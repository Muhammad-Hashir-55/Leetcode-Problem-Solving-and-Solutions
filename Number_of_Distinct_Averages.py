class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        while(nums):
            mini = min(nums)
            nums.remove(mini)
            maxi = max(nums)
            nums.remove(maxi)
            s.add((mini + maxi)/2)
        n = len(s)
        return n
        

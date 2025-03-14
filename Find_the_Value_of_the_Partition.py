class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        diff = []
        n = len(nums)
        for i in range(n-1):
            diff.append(nums[i+1] - nums[i])
        return min(diff)

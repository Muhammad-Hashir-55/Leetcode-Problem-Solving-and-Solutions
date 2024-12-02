class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans
        

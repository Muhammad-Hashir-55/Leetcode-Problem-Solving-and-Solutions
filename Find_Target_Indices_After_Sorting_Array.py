class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if(nums[i]== target):
                ans.append(i)
        return ans


        

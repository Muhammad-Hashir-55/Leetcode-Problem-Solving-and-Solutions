class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs= []
        while(nums):
            pairs.append([nums[0],nums[-1]])
            nums.pop()
            nums.pop(0)
        
        maxi = 0
        for i in pairs:
            maxi = max(maxi,i[0]+i[1])
        return maxi
        

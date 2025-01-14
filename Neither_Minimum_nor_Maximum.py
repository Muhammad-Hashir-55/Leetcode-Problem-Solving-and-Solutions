class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        x = -1


        for i in nums:
            if(i != mini and i != maxi):
                x = i
                break
        return x
        

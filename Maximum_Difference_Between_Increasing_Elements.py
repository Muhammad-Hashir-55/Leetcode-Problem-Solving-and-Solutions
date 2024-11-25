class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi = -1
        n =len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]<nums[j]):
                    diff = nums[j]- nums[i]
                    if(diff >maxi):
                        maxi = diff
        return maxi
        

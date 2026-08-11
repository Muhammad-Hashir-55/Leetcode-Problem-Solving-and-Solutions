class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
    
        sumi = nums[0]
        num = 0
        for i in range(1,n):
            if(nums[i]- nums[i-1]==1):
                sumi +=nums[i]
            else:
                break
        num = sumi
        while(num in nums):
            num +=1
        return num

        

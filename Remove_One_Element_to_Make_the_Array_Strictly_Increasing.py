# oh finally

class Solution:
    def canBeIncreasing(self, nums) -> bool:
        n = len(nums)
        if(n ==2):
            return True
        c = False
        for i in range(1,n-1):
            if(nums[i]<nums[i-1] and nums[i]<nums[i+1] and nums[i-1]<nums[i+1]):
                nums.pop(i)
                c= True
                break
            elif(nums[i]>nums[i+1] and nums[i]>nums[i+1] and nums[i-1]<nums[i+1]):
                nums.pop(i)
                c = True
                break
        n = len(nums)
        if(nums[-1]<nums[-2] and c== False):
            nums.pop(n-1)
            c = True
        if(c== False):
            n = len(nums)
            for i in range(n-1):
                if(nums[i]>=nums[i+1]):
                    nums.pop(i)
                    break

            
        n = len(nums)
        for i in range(n-1):
            if(nums[i]>=nums[i+1]):
                return False
        return True

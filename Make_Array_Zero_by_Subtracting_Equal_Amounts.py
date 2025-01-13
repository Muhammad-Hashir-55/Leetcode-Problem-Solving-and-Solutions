class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c =0
        while(sum(nums)!=0):
            x= 99999999
            for i in range(n):
                if(nums[i]<x and nums[i]>0):
                    x = nums[i]
            for i in range(n):
                if(nums[i]==0):
                    continue
                nums[i] -=x
            c +=1
        return c


        

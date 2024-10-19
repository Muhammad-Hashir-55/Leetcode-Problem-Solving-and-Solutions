class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums= [0]*(n+1)
        nums[0] = 0
        if(n+1==1):
            return max(nums)
        nums[1] = 1
        number = 2
        i=1
        number= 2
        while(nums[-1]==0):
            if(nums[-1]!=0):
                break
            nums[number*i]= nums[i]
            if(nums[-1]!=0):
                break
            nums[number*i +1] = nums[i]+nums[i+1]
            i +=1
            
        return max(nums)

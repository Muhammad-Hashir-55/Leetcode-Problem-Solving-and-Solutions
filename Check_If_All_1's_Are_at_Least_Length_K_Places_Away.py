class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        started = False
        com = 0
        if(1 not in nums):
            return True
        indexx = nums.index(1)
        started = True
        
        for i in range(indexx,len(nums)):
            if(nums[i]==0):
                com +=1
            if(nums[i] ==1 and i!=indexx):
                if(com<k):
                    return False
                com =0
        return True


check = Solution()
print(check.kLengthApart([1,0,0,0,1,0,0,1],2))

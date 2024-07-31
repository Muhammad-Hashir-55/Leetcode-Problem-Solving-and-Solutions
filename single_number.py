class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in nums:
            if (nums.count(i) ==1):
                return i
        
            
check =Solution()
print(check.singleNumber([1,3,1,-1,3]))

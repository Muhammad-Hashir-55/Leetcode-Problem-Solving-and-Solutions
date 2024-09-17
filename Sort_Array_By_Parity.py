class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums) ==1):
            return nums
        l1 =[]
        for i in nums:
            if(i % 2 ==0):
                l1.append(i)
        l2 =[]
        for j in nums:
            if(j % 2 != 0):
                l2.append(j)
        return l1+l2        

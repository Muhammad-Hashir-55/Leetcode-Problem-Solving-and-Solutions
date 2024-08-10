class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = len(nums)
        for i in nums[:]:
            if(i == 0):
                nums.remove(i)
        while(len(nums) != index):
            nums.append(0)
        
        
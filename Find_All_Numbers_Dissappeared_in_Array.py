class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        n = len(nums)
        num_set = set(nums)
        for i in range(1,n+1):
            if (i not in num_set):
                new_list.append(i)
        if (not new_list):
            return new_list
        else:
            return new_list
        
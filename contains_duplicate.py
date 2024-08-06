class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_set = set()
        for i in nums:
            if (i in new_set):
                return True
            new_set.add(i)
        return False

        
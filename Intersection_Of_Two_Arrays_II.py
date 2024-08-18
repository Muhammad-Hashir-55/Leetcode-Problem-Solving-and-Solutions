class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = []
        if(len(nums1)>len(nums2)):
            nums1,nums2 = nums2,nums1

        for i in nums1:
            if(i in nums2):
                common.append(i)
                nums2.remove(i)
        return common
        
        
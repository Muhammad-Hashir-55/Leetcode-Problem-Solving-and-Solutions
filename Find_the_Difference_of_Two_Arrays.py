class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        big_list= []
        distinct_ns1 =[]
        distinct_ns2 = []
        for i in nums1:
            if(i not in nums2 and i not in distinct_ns1):
                distinct_ns1.append(i)
        for j in nums2:
            if(j not in nums1 and j not in distinct_ns2):
                distinct_ns2.append(j)
        big_list.append(distinct_ns1)
        big_list.append(distinct_ns2)
        return big_list
        

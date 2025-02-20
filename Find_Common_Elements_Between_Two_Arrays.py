class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        c1 =0
        for i in nums1:
            if(i in nums2):
                c1 +=1
        common.append(c1)
        c2= 0
        for i in nums2:
            if(i in nums1):
                c2 +=1
        common.append(c2)
        return common

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        x1= min(nums1)
        x2 = min(nums2)
        s = set()
        for i in nums1:
            if(i in nums2):
                s.add(i)
        for i in nums2:
            if(i in nums1):
                s.add(i)
        if(s):
            return min(s)
        if(x1<x2):
            return x1*10 + x2
        elif(x2<x1):
            return x2*10 + x1
        else:
            return x1
        

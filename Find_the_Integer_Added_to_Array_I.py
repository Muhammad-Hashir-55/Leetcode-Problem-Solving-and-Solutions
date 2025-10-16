class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        mini1 = min(nums1)
        mini2 = min(nums2)
        return mini2 - mini1
        

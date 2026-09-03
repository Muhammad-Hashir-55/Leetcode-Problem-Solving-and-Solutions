class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        sm = float('inf')
        for i in nums1:
            if(i% 2 != 0):
                sm = min(sm,i)
        if(sm == float('inf')):
            return True
        for i in nums1:
            if(i % 2 == 0 and i <=sm):
                return False
        return True
        

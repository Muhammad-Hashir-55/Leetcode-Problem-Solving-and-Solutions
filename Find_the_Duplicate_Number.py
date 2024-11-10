class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lis = set()
        for i in nums:
            if(i not in lis):
                lis.add(i)
            else:
                return i
        

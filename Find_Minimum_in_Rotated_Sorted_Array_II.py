class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 999999
        for i in nums:
            if(i <mini):
                mini = i
        return mini

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxi = 0
        for i in nums:
            if(i>0):
                if(maxi<i and -i in nums):
                    maxi = i
        if(maxi == 0):
            return -1
        else:
            return maxi

        

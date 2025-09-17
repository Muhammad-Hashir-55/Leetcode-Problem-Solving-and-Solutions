class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        coun = 0
        for i in nums:
            if(i < k):
                coun +=1
        return coun
        

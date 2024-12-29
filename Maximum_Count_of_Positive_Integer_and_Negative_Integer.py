class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        for i in nums:
            if(i<0):
                x1 +=1
            elif(i>0):
                x2 +=1
        return max(x1,x2)
        

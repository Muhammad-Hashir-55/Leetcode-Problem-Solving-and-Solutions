class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        index = 0
        for i in nums:
            sum1 = 0
            sum2 = 0
            sum1 = sum(nums[:index])
            sum2 = sum(nums[index+1:])
            if(sum1 == sum2):
                return index
            index += 1
        return -1
        

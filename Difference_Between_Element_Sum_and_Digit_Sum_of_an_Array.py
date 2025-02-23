class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumi1 = sum(nums)
        s = ''
        for i in nums:
            s += str(i)
        sumi2 = 0
        for i in s:
            sumi2 += int(i)
        return abs(sumi1 - sumi2)
    
        
        

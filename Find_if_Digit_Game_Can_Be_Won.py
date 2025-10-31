class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumi1 = 0
        sumi2 = 0
        for i in nums:
            if(i>=10):
                sumi1 +=i
            else:
                sumi2 +=i
        if(sumi1 == sumi2):
            return False
        return True
        

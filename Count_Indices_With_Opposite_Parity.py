class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        count_o = 0
        count_e = 0
        ans = []
        for i in nums:
            if(i %2 == 0):
                count_e +=1
            else:
                count_o +=1
        
        for i in nums:
            if(i % 2 == 0):
                ans.append(count_o)
                count_e -=1
            else:
                ans.append(count_e)
                count_o -=1
        return ans
        

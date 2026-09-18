class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ss = set()
        xor = 0
        for i in nums:
            if(i in ss):

                xor = xor^i
            ss.add(i)
        return xor


            
        

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sumi = 0
        n = len(nums)
        for i in range(n):
            bina = bin(i)
            ones = bina.count('1')
            if(ones == k):
                
                sumi +=nums[i]
        return sumi
        

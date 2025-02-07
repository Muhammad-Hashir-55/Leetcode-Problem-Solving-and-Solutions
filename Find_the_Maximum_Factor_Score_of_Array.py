from math import gcd,lcm
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        arr = []
        n = len(nums)
        gc = gcd(*nums)
        lc = lcm(*nums)
        arr.append(gc * lc)

        for i in range(n):
            x = []
            for j in range(n):
                if(j ==i):
                    continue
                else:
                    x.append(nums[j])
            gc= gcd(*x)
            lc = lcm(*x)
            arr.append(gc * lc)
        return max(arr)
        


        

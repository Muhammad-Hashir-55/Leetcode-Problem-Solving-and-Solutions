class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_s(li):
            res = li[0]
            for i in li[1:]:
                res = res^i
            return res
        
        from itertools import combinations
        sumi = sum(nums)

        n = len(nums)
        for i in range(2,n+1):
            x = list(combinations(nums,i))
            for j in x:
                sumi += xor_s(j)
        return sumi
        

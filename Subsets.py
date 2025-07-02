class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        from itertools import combinations
        bg = []
        for i in range(0,n+1):
            x = list(combinations(nums,i))
            for j in x:
                bg.append(j)
        return bg
        

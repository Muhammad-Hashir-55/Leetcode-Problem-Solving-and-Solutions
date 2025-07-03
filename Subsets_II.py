from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ss = set()
        bg = []
        n = len(nums)
        for i in range(0,n+1):
            x = list(combinations(nums,i))
            if(() in x):
                bg.append(())
                continue
            for j in x:
                l = tuple(sorted(j))
                if(l not in ss):
                    bg.append(l)
                    ss.add(l)
        return bg

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        curr = float('inf')
        res = []
        for i in cost:
            if(curr>i):
                curr = i
                res.append(curr)
            else:
                res.append(curr)
        return res
        

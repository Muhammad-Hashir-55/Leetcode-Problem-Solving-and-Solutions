from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        x = list(combinations(range(1,n+1),k))
        
        return x

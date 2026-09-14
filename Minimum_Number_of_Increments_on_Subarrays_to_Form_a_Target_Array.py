class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        ans = 0
        for i in target:
            if(i>prev):
                ans += i - prev
            prev = i
        return ans
        

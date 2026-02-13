class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(-1)
            for j in range(i):
                if(j | (j +1) == i):
                    ans[-1] = j
                    break
        return ans

        

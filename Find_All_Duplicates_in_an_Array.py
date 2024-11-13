class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for i in nums:
            if(i in seen):
                ans.append(i)
            else:
                seen.add(i)
        return ans
        

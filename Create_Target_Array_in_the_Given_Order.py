class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        ii = 0
        for i in nums:
            ans.insert(index[ii],i)
            ii +=1
        return ans
        

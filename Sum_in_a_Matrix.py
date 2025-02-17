class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        score = 0
        m = len(nums[0])
        ii = 0
        while(ii <m):
            arr = []
            for i in nums:
                maxi = max(i)
                arr.append(maxi)
                i.remove(maxi)
            score = score + max(arr)
            ii +=1
        return score

        

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n+1):
            for j in range(0,n):
                xx = nums[j:j+i]
                if(len(xx) != i):
                    continue
                ss = set(xx)
                sq = len(ss)
                ans += sq**2
        return ans
                


        

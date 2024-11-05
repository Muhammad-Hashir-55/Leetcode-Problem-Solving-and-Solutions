class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cc = 0
        for i in range(n):
            for j in range(i+1,n):
                if(abs(nums[i]-nums[j])==k):
                    cc +=1
        return cc
        

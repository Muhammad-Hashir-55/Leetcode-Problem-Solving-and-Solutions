class Solution:
    def specialArray(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans = 0

        while(ans <= maxi):
            count = 0
            for i in nums:
                if(i>=ans):
                    count +=1
            if(count == ans):
                return ans
            else:
                ans +=1
        return -1



        

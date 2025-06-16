class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            tot = 0
            left = 0
            odd_count = 0
            for right in range(len(nums)):
                if(nums[right] % 2 != 0 ):
                    odd_count +=1
                while(odd_count > k):
                    if(nums[left] % 2 != 0):
                        odd_count -=1
                    left +=1
                tot += right - left +1
            return tot
        return atmost(k) - atmost(k -1)

        

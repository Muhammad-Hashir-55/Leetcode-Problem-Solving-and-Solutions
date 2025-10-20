class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while(len(nums) != 1):
            x = []
            for i in range(1,len(nums)):
                x.append((nums[i] + nums[i-1]) % 10)
            nums = x
        print(nums)
        return nums[-1]

            

        

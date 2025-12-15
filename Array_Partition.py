class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        bg = []
        n = len(nums)
        for i in range(0,n-1,2):
            x = []
            x.append(nums[i])
            x.append(nums[i+1])
            bg.append(x)
        
        mini = 0
        for i in bg:
            x = min(i)
            mini +=x
        return mini
        

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if(nums == sorted(nums)):
            return True
        for i in range(n):
            nums.insert(0,nums[-1])
            nums.pop()
            if(nums == sorted(nums)):
                return True
        else:
            return False
            
        

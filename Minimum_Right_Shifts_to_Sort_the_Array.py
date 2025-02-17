class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        store = nums[:]
        store.sort()
        n= len(nums)
        c = 0
        if(nums == store):
            return 0
        for i in range(n):
            c +=1
            x = nums[-1]
            nums.insert(0,x)
            nums.pop()
            if(nums == store):
                return c
        return -1
        

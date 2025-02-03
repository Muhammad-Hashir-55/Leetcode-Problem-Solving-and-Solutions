class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        indexes = []
        while(target in nums):
            idx = nums.index(target)
            nums[idx] = -1
            indexes.append(idx)
        print(indexes)
        mini = 999999
        for i in indexes:
            if(mini > abs(i - start)):
                mini = abs(i - start)
        return mini
        

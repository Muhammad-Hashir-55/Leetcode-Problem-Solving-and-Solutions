class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        maxi = max(nums)
        maxi += -k
        mini +=k
        x = maxi - mini
        if(x <0):
            return 0
        else:
            return x
        

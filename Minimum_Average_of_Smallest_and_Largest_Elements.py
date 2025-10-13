class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        avgs =[] 
        for i in range(n//2):
            x1= nums.pop(0)
            x2 = nums.pop()
            avgs.append((x1 + x2)/2)
        return min(avgs)
        

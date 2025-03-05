class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr= []
        for i in range(n):
            x1 = nums[:i+1]
            x2 = nums[i+1:]
            arr.append(len(set(x1))    - len(set(x2)))
        return arr
        

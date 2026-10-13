class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i in nums:
            arr.append(abs(i))
        nums = arr
        nums.sort()
        sumi = 0
        st = n//2
        for i in nums[st:]:
            sumi += i**2
        print(sumi)
        for i in nums[:st]:
            sumi -= i**2
        return sumi
        

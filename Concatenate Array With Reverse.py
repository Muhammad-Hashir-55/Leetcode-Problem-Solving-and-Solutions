class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        new_nums = nums[:]
        for i in nums[::-1]:
            new_nums.append(i)
        return new_nums

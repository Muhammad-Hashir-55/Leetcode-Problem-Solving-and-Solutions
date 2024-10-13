class Solution:
    def sumOfUnique(self, nums) -> int:
        new_list = []
        for i in nums:
            if(nums.count(i)==1):
                new_list.append(i)
        return sum(new_list)

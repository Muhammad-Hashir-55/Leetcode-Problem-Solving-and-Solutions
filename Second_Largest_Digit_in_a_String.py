class Solution:
    def secondHighest(self, s: str) -> int:
        my_set = set()
        for i in s:
            if(i.isalpha()==False):
                my_set.add(int(i))
        
        nums = list(my_set)
        if(not nums):
            return -1
        maxi = nums[0]

        for i in nums[1:]:
            if(i>maxi):
                maxi = i
        nums.remove(maxi)
        if(not nums):
            return -1
        maxi = nums[0]
        for i in nums[1:]:
            if(i>maxi):
                maxi = i
        return maxi

        

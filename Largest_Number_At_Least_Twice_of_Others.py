class Solution:
    def dominantIndex(self, nums) -> int:
        maxi = nums[0]
        for i in nums[1:]:
            if(i>maxi):
                maxi = i
        
        if(nums.count(maxi)>1):
            return -1

        new_list = []
        for k in nums:
            new_list.append(k)

        nums.remove(maxi)
  

        for j in nums:
            if(maxi< 2*j):
                return -1

        return new_list.index(maxi)

        

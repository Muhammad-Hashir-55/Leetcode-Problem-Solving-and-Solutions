class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        new_list = []
        n = len(nums)
        index = 0
        if(not new_list):
            sum1= 0
        sum2 = sum(nums[index+1:])
        if(sum1 == sum2):
            return index
        for i in range(n):
            new_list.append(nums[i])
            index+=1
            sum1 = sum(new_list)
            if(index == n):
                break
            sum2 = sum(nums[index+1:])
            if(sum1 == sum2):
                return index
        return -1
        

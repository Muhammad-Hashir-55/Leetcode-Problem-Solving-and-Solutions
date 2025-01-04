class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr  =[]
        n = len(nums)
        for i in range(n-1):
            if(nums[i]==nums[i+1]):
                nums[i]= nums[i]*2
                nums[i+1] = 0
        for i in nums:
            if(i !=0):
                arr.append(i)
        while(len(arr)!= n):
            arr.append(0)
        return arr
        
        

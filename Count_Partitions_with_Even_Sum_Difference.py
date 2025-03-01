class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            arr1 = nums[:i+1]
            arr2 = nums[i+1:]
            if(not arr1 or not arr2):
                break
            x = sum(arr1) - sum(arr2)
            if(x %2 == 0):
                c +=1
        return c

        

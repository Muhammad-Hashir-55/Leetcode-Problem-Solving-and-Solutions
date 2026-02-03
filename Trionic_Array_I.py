class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if(nums[0] >= nums[1]):
            return False
        n = len(nums)
        
        p = -1
        for i in range(1,n):
            if(nums[i-1]>nums[i]):
                p = i-1
                break
            elif(nums[i-1] == nums[i]):
                return False
            else:
                continue
        if(i == n-1):
            print('ha1')
            return False
        q= -1
        for i in range(p+1,n):
            if(nums[i-1]<nums[i]):
                q = i-1
                break
            elif(nums[i-1] == nums[i]):
                return False
            else:
                continue
        arr = nums[q:]
        print(arr)
        if(len(arr)<2):
            print('ha2')
            return False
        n = len(arr)
        for i in range(1,n):
            if(arr[i-1] == arr[i]):
                return False
        return sorted(arr) == arr
        




        
        

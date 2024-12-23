class Solution:
    def separateDigits(self, nums):
        arr = []
        n= len(nums)
        for i in range(n):
            x = []
            while(nums[i] >=10):
                x.append(nums[i]%10)
                nums[i] = nums[i]//10
            arr.append(nums[i])
            for j in x[::-1]:
                arr.append(j)
        return arr


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        maxi = max(nums)
        n = len(nums)
        arr = []
        store = nums[:]
        
        for i in store:
            nums.append(i)
        
        m = len(nums)

        for i in range(n):
            if(nums[i] == maxi):
                arr.append(-1)
                continue
            for j in range(i+1,m):
                if(nums[j]> nums[i]):
                    x= nums[j]
                    break
            arr.append(x)
        return arr

        

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr  =[]
        while(nums):
            x1 = min(nums)
            nums.remove(x1)
            x2 = min(nums)
            nums.remove(x2)
            arr.append(x2)
            arr.append(x1)
        return arr
            
        

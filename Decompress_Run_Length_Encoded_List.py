class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(0,n,2):
            for j in range(nums[i]):
                arr.append(nums[i+1])
        return arr

        

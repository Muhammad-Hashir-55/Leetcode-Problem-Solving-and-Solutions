class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        big_l = [0] *(2*n)
        for i in range(n):
            big_l[i] = nums[i]
        ii = 0
        for i in range(n,2*n):
            big_l[i] = nums[ii]
            ii +=1
        return big_l

        

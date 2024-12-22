class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        i_map = {}
        for i in range(n):
            i_map[nums[i]] = i
        for old,new in operations:

            idx = i_map[old]
            nums[idx] = new
            i_map[new] = idx
            del i_map[old]
        return nums
        

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        bg = nums[:]
        for i in nums:
            s = str(i)
            x = int(s[::-1])
            bg.append(x)
        s = set()
        for i in bg:
            s.add(i)
        n = len(s)
        return n
        

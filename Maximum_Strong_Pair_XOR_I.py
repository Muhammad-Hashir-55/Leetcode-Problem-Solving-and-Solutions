class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            for j in nums:
                if(abs(i-j)<=min(i,j)):
                    arr.append(i^j)
        return max(arr)

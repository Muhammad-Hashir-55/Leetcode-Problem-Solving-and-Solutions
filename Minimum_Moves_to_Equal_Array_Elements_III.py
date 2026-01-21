class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        moves = 0
        for i in nums:
            x = maxi - i
            moves +=x
        return moves
    
        

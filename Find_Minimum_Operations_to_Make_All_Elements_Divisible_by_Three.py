class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_ops = 0
        for i in nums:
            if(i %3 ==0):
                continue
            elif((i -1) % 3 == 0):
                min_ops += 1
            elif((i+1) % 3 == 0):
                min_ops +=1
            else:
                min_ops +=2
        return min_ops
        

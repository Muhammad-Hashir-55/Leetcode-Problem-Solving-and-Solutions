class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict

        n = len(nums)
        c = 0
        pc = defaultdict(int)
    
        for i in range(n):
            for j in range(i+1,n):
                prd = nums[i]*nums[j]
                c = c + 8 * pc[prd]
                pc[prd] +=1
        
        return c
        



        
        

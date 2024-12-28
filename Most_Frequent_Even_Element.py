class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
    
        ans = -1
        c= -2
        nums.sort()
        for i in nums:
            if(i%2 ==0 and nums.count(i)>c):
                ans = i
                c= nums.count(i)
        return ans
        
        

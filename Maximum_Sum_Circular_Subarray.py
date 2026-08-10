class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        
        maxi = float('-inf')
        mini = float('inf')
        curr_maxi = 0
        curr_mini = 0
        tot = 0
        for i in nums:
            tot +=i
            curr_maxi +=i
            maxi = max(maxi, curr_maxi)
            if(curr_maxi <0):
                curr_maxi = 0
            
            curr_mini +=i
            mini = min(mini,curr_mini)
            if(curr_mini >0):
                curr_mini = 0


        if(maxi <0):
            return maxi
                
        return max(maxi,tot - mini)


        

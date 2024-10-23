class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        if(maxi %mini ==0):
            return mini
        else:
            n = mini
            while(True):
                if(maxi%n ==0 and mini %n ==0):
                    return n
                n -=1
        

class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        curr = 0
        for i in s:
            if(i == '('):
                curr +=1
            elif(i == ')'):
                curr -=1
            maxi = max(maxi,curr)
        return maxi


        

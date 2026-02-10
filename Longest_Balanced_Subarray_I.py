class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxi = 0
        n = len(nums)
        for i in range(n):
            nn = 1
            s1 = set()
            s2 = set()
            if(nums[i]%2 == 0):
                s1.add(nums[i])
            else:
                s2.add(nums[i])
            for j in range(i+1,n):
                nn +=1
                if(nums[j]%2 == 0):
                    s1.add(nums[j])
                else:
                    s2.add(nums[j])
                if(len(s1) == len(s2)):
                    maxi = max(nn,maxi)

        return maxi
                    
                

        

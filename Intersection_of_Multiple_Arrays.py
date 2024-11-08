class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        maxi = -1
        for i in nums:
            for j in i:
                if(j>maxi):
                    maxi = j
        ans = []
        nn = 0
        while(nn <=maxi):
            c = False
            for i in nums:
                if(nn in i):
                    c = True
                    continue
                else:
                    c = False
                    break
            if(c == True):
                ans.append(nn)
            nn +=1
        return ans


        

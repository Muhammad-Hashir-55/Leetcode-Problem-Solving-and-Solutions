class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        ans = []
        for i in dic:
            if(dic[i]==1 and i-1 not in dic and i+1 not in dic):
                ans.append(i)
        return ans

        

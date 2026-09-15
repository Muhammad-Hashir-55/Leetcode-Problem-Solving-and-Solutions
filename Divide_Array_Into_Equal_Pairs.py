class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if(i not in dic):
                dic[i] = 0
            dic[i] +=1
        for i in dic:
            if(dic[i] % 2 != 0):
                return False
        return True
        

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        arr = []
        for i in nums:
            if(i in dic):
                arr.append(i)
            else:
                dic[i] =1
        return arr
        

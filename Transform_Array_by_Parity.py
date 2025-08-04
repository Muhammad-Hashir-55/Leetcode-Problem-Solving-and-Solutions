class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        dic = {0:0,1:0}
        for i in nums:
            if(i % 2 == 0):
                dic[0] +=1
            else:
                dic[1] +=1
        arr = []
        for i in dic:
            for j in range(dic[i]):
                arr.append(i)
        return arr
        
        

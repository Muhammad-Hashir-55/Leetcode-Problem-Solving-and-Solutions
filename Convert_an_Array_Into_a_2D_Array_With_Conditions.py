class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] =1
        maxi = 0
        for i in dic:
            if(dic[i] > maxi):
                maxi = dic[i]
        num_rows = maxi
        bg = []
        for i in range(num_rows):
            arr = []
            for j in dic:
                if(dic[j] >0):
                    arr.append(j)
                    dic[j] -=1
            bg.append(arr)
        return bg
        

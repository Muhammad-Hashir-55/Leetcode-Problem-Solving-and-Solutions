class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] =1
        maxi = -1
        for i in dic:
            if(dic[i]>maxi):
                maxi = dic[i]
        a = []
        for i in dic:
            if(dic[i] == maxi):
                a.append(i)
        print(a)
        b = []

        for i in a:
            c = 0
            idx = nums.index(i)
            leng = 0
            while(c != dic[i]):
                if(nums[idx] == i):
                    c +=1
                leng +=1
                idx +=1
            b.append(leng)
        return min(b)
                

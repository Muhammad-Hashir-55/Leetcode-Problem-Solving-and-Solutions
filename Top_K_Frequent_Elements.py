class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        for i in nums:
            if(i not in dic):
                dic[i] =1
            else:
                dic[i] +=1
        l = []
        for i in dic:
            x= []
            x.append(dic[i])
            x.append(i)
            l.append(x)
        #print(dic)
        #print(l)
        ll = sorted(l,reverse=True)
        #print(ll)
        arr= []
        for i in range(k):
            arr.append(ll[i][1])
        return arr

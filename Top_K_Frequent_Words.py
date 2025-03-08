class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i in words:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] = 1
        arr = []
        for i in range(k):
            maxi = -1
            
            for j in dic:
                if(j not in arr and dic[j]>maxi):
                    maxi = dic[j]
            x = []
            for j in dic:
                if(dic[j] == maxi):
                    x.append(j)
            x.sort()
            for j in x:
                if(j not in arr):
                    arr.append(j)
                    break
            
        
        return arr


        

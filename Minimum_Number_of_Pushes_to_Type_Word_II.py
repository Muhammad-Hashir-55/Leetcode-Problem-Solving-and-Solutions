class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = {}
        for i in word:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] = 1
        arr = []
        while(dic):
            maxi = -1
            idx = ''
            for i in dic:
                if(dic[i]>maxi):
                    maxi = dic[i]
                    idx = i
            x = [idx,maxi]
            del dic[idx]
            arr.append(x)


        idx = 0
        count = 0
        mul = 1
        for i in arr:
            idx +=1
            count = count + (i[1]*mul)
            if(idx % 8 == 0):
                mul +=1
        return count
            





        

class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1,n+1):
            x = str(i)
            sumi = 0
            for j in x:
                sumi = sumi + int(j)
            if(sumi in dic):
                dic[sumi] +=1
            else:
                dic[sumi]= 1
        x = dic.values()
        print(dic)
        print(x)
        maxi = max(x)
        c =0
        for i in x:
            if(i == maxi):
                c +=1
        return c

        

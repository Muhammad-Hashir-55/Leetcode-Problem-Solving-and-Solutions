class Solution:
    def maxDifference(self, s: str) -> int:
        dic ={}
        for i in s:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] = 1
        x1= []
        x2 = []
        for i in dic:
            if(dic[i]% 2 == 0):
                x1.append(dic[i])
            else:
                x2.append(dic[i])
        mini1 = min(x1)
        maxi2 = max(x2)

        return maxi2 - mini1
        

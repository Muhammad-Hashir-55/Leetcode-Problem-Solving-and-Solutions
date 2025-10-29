class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic1 = {}
        dic2 = {}
        for i in s:
            if(i in dic1):
                dic1[i] +=1
            else:
                dic1[i] = 1
        for i in t:
            if(i in dic2):
                dic2[i] +=1
            else:
                dic2[i] =1
        if(dic1 == dic2):
            return 0
        count  = 0
        
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        for i in alphas:
            if(i in dic1):
                if(i not in dic2):
                    count += dic1[i]
                elif(dic1[i] > dic2[i]):
                    count += abs(dic1[i] - dic2[i])

        
        
            

        return count

        

class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = {}
        for i in s:
            if(i not in dic):
                dic[i] = 1
            else:
                dic[i] +=1
        maxi_v = 0
        for i in 'aeiou':
            if(i not in dic):
                continue
            if(dic[i] > maxi_v):
                maxi_v= dic[i]
        maxi_c = 0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if(i not in dic):
                continue
            if(i in 'aeiou'):
                continue
            if(dic[i] > maxi_c):
                maxi_c = dic[i]
        return maxi_v + maxi_c

        

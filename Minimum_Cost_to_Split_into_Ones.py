class Solution:
    def minCost(self, n: int) -> int:
        dic = {1:0,2:1,3:3,4:6}
        if(n == 1):
            return 0
        if(n in dic):
            return dic[n]
        for i in range(5,n+2):
            if(n in dic):
                return dic[n]
            dic[i] = ((i-1) * 1) + dic[i-1]
        

        

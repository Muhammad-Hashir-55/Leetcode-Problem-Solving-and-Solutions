class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic ={}
        maxi_b = -1
        maxi = -1
        for i in range(lowLimit, highLimit+1):
            x = str(i)
            sumi = 0
            for j in x:
                sumi += int(j)
            if(sumi not in dic):
                dic[sumi] = 1
                maxi = max(maxi,1)
                
            else:
                dic[sumi] +=1
                maxi = max(maxi,dic[sumi])
            
            if(dic[sumi] == maxi):
                maxi_b = sumi
        return maxi

        

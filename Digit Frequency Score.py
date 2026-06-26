class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        stri = str(n)
        dic = {}
        for i in stri:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] = 1
        tot = 0
        for i in dic:
            tot += (int(i)* dic[i])
        return tot
        

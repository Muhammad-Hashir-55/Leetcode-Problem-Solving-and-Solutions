class Solution:
    def countEven(self, num: int) -> int:
        nn = 2
        ans = 0
        while(nn<=num):
            s= str(nn)
            summ = 0
            for i in s:
                summ = summ + int(i)
            if(summ %2 ==0):
                ans +=1
            nn +=1
        return ans

        

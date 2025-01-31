class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if(k %2 ==0 or k %5 ==0):
            return -1
        n=1
        l = 1
        while(True):
            if(n % k ==0):

                return l
            l +=1
            n= 10*n +1

class Solution:
    def fib(self, n: int) -> int:
        if(n ==0):
            return 0
        if(n==1):
            return 1
        l = [0]*(n+1)
        l[0]=  0
        l[1] = 1

        for i in range(2,len(l)):
            l[i] = l[i-1]+ l[i-2]
        return l[n]

        

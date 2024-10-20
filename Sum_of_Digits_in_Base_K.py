class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if(k==10):
            s=  str(n)
            summ = 0
            for i in s:
                summ = summ+ int(i)
            return summ
        else:
            new_num=  ""
            while(n>0):
                mod = n%k
                new_num = new_num +str(mod)
                n = n//k
            summ= 0
            for i in new_num:
                summ = summ + int(i)
            return summ
        
        

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if(dividend<0)^(divisor<0) else 1
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        while(a>=b):
            temp = b
            multiple = 1
            while(a>= temp<<1):
                temp <<=1
                multiple <<=1
            a -=temp
            ans +=multiple
        final = ans *sign
        if(final>2**31-1):
            return 2**31 -1
        elif(final<-2**31):
            return -2**31
        else:
            return final
        

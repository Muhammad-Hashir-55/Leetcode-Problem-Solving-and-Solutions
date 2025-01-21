class Solution:
    def rotatedDigits(self, n: int) -> int:
        c= 0
        nums = {'0':'0','1':'1','2':'5','5':'2','6':'9','9':'6','8':'8'}
        invalids = '347'
        for i in range(n+1):
            x = str(i)
            xx = ''
            for j in x:
                if(j in invalids):
                    break
                if(j in nums):
                    xx = xx + nums[j]
                else:
                    xx +=j
            if(xx != x and len(x)==len(xx)):
                c +=1

        return c
        

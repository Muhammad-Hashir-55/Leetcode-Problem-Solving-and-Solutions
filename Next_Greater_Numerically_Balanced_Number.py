class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n+1
        while(True):
            xx = str(x)
            c = True
            for i in xx:
                if(xx.count(i)== int(i)):
                    continue
                else:
                    c = False
                    break
            if(c== True):
                return int(xx)
            x +=1
        

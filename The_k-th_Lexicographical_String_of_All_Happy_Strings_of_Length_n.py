from itertools import product
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = 'abc'
        lis = product(s,repeat=n)

        arr = []
        for i in lis:
            x =('').join(i)
            
            if('aa' in x or 'bb' in x or 'cc' in x):
                continue
            else:
                arr.append(x)
        del lis
        
        
        if(len(arr)<k):
            return ''
        return arr[k-1]

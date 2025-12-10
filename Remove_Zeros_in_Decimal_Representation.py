class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n)
        ss = ''
        for i in s:
            if(i != '0'):
                ss +=i
        return int(ss)
        

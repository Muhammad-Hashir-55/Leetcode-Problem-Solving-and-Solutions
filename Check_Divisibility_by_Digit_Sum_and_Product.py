class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        n1 = 0
        n2 = 1
        for i in s:
            x = int(i)
            n1 +=x
            n2 *=x
        num = n1 + n2
        if(n % num == 0):
            return True
        else:
            return False
        

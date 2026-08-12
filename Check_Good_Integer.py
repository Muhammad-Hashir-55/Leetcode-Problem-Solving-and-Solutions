class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s = str(n)
        simple = 0
        sq = 0
        for i in s:
            x = int(i)
            sqq = x*x
            simple +=x
            sq +=sqq
        
        if(sq - simple >=50):
            return True
        else:
            return False

        

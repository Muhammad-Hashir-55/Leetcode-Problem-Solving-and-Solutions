class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        s = s[::-1]
        s = int(s)
        s = str(s)
        ss = int(s[::-1])
        if(ss == num):
            return True
        else:
            return False
        

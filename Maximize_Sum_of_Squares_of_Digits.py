class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = ''
        chk = 9*num
        if(sum > chk):
            return ''
        while(sum >0):
            if(sum <9):
                s += str(sum)
                sum = 0
            else:
                s +='9'
                sum -=9
        while(len(s) != num):
            s +='0'
        return s
        
